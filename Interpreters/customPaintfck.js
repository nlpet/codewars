/*
Esolang Interpreters #3 - Custom Paintfuck Interpreter

About this Kata Series

"Esolang Interpreters" is a Kata Series that originally began as three separate,
independent esolang interpreter Kata authored by @donaldsebleung which all shared a
similar format and were all somewhat inter-related. Under the influence of a fellow
Codewarrior, these three high-level inter-related Kata gradually evolved into what
is known today as the "Esolang Interpreters" series.

This series is a high-level Kata Series designed to challenge the minds of bright
and daring programmers by implementing interpreters for various esoteric programming
languages/Esolangs, mainly Brainfuck derivatives but not limited to them, given a
certain specification for a certain Esolang. Perhaps the only exception to this
rule is the very first Kata in this Series which is intended as an introduction/taster
to the world of esoteric programming languages and writing interpreters for them.

The Language

Paintfuck is a borderline-esoteric programming language/Esolang which is a
derivative of Smallfuck (itself a derivative of the famous Brainfuck) that uses
a two-dimensional data grid instead of a one-dimensional tape.

Valid commands in Paintfuck include:

n - Move data pointer north (up)
e - Move data pointer east (right)
s - Move data pointer south (down)
w - Move data pointer west (left)
* - Flip the bit at the current cell (same as in Smallfuck)
[ - Jump past matching ] if bit under current pointer is 0 (same as in Smallfuck)
] - Jump back to the matching [ (if bit under current pointer is nonzero)

The specification states that any non-command character (i.e. any character other
than those mentioned above) should simply be ignored. The output of the interpreter
is the two-dimensional data grid itself, best as animation as the interpreter is
running, but at least a representation of the data grid itself after a certain
number of iterations (explained later in task).

In current implementations, the 2D datagrid is finite in size with toroidal
(wrapping) behaviour. This is one of the few major differences of Paintfuck
from Smallfuck as Smallfuck terminates (normally) whenever the pointer exceeds
the bounds of the tape.

Similar to Smallfuck, Paintfuck is Turing-complete if and only if the 2D data
grid/canvas were unlimited in size. However, since the size of the data grid
is defined to be finite, it acts like a finite state machine.

More info on this Esolang can be found here.

The Task

Your task is to implement a custom Paintfuck interpreter interpreter() which
accepts the following arguments in the specified order:

* code - Required. The Paintfuck code to be executed, passed in as a string. May
  contain comments (non-command characters), in which case your interpreter should
  simply ignore them. If empty, simply return the initial state of the data grid.
* iterations - Required. A non-negative integer specifying the number of iterations to be
  performed before the final state of the data grid is returned. See notes for definition
  of 1 iteration. If equal to zero, simply return the initial state of the data grid.
* width - Required. The width of the data grid in terms of the number of data cells in
  each row, passed in as a positive integer.
* height - Required. The height of the data grid in cells (i.e. number of rows) passed
  in as a positive integer.

A few things to note:

* Your interpreter should treat all command characters as case-sensitive so N, E,
  S and W are not valid command characters
* Your interpreter should initialize all cells within the data grid to a value of
  0 regardless of the width and height of the grid
* In this implementation, your pointer must always start at the top-left hand
  corner of the data grid (i.e. first row, first column). This is important as
  some implementations have the data pointer starting at the middle of the grid.
* One iteration is defined as one step in the program, i.e. the number of command
  characters evaluated. For example, given a program nessewnnnewwwsswse and an
  iteration count of 5, your interpreter should evaluate nesse before returning
  the final state of the data grid. Non-command characters should not count towards
  the number of iterations.
* Regarding iterations, the act of skipping to the matching ] when a [ is encountered
  (or vice versa) is considered to be one iteration regardless of the number of command
  characters in between. The next iteration then commences at the command right after
  the matching ] (or [).
* Your interpreter should terminate normally and return the final state of the 2D
  data grid whenever any of the mentioned conditions become true: (1) All commands
  have been considered left to right, or (2) Your interpreter has already performed
  the number of iterations specified in the second argument.
* The return value of your interpreter should be a representation of the final
  state of the 2D data grid where each row is separated from the next by a CRLF
  (\r\n). For example, if the final state of your datagrid is

[
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]

... then your return string should be "100\r\n010\r\n001".

*/

function flipBit(bit) {
  return bit === '0' ? '1' : '0';
}


function getLoops(code) {
  const sf = {};
  const sb = {};
  const stack = [];

  code.split('').forEach( (cmd, i) => {
    if (cmd === '[') {
      stack.push(i);
    } else if (cmd === ']') {
      const el = stack.pop();
      sf[el] = i;
      sb[i] = el;
    }
  });

  return [sf, sb];
}


function zeroes(dimensions) {
    var array = [];

    for (var i = 0; i < dimensions[0]; ++i) {
        array.push(dimensions.length === 1 ? 0 : zeroes(dimensions.slice(1)));
    }
    return array;
}


function convertToString(grid, sep) {
  for (let i = 0; i < grid.length; i++) {
    grid[i] = grid[i].join('');
  }
  return grid.join(sep);
}


function cleanUp(code) {
  const re = /[nswe\*\[\]]/g;
  const match = code.match(re);
  if (match) {
    return match.join('');
  }
  return '';
}


function interpreter(code, iterations, width, height) {
  let ptrw = 0;
  let ptrh = 0;
  let i = 0;
  const re = /[nswe*\[\]]/;

  code = cleanUp(code);
  const grid = zeroes([height, width]);
  const [sf, sb] = getLoops(code);

  if (!code.length) { return convertToString(grid, '\r\n'); }

  while (i < iterations) {
    const ch = code[i];

    if (ch === 'n') {
      ptrh --;
      if (ptrh < 0) { ptrh = height - 1; }
    }
    else if (ch === 'e') {
      ptrw ++;
      if (ptrw === width) { ptrw = 0; }
    }
    else if (ch === 's') {
      ptrh ++;
      if (ptrh === height) { ptrh = 0; }
    }
    else if (ch === 'w') {
      ptrw --;
      if (ptrw < 0) { ptrw = width - 1; }
    }
    else if (ch === '*') { grid[ptrh][ptrw] = flipBit(grid[ptrh][ptrw]); }
    else if (ch === '[') {
      if (grid[ptrh][ptrw] === '0') {
        i = sf[i] + 1;
        continue;
      }
    }
    else if (ch === ']') {
      if (grid[ptrh][ptrw] === '1') {
        i = sb[i] + 1;
        continue;
      }
    }
    i ++;
  }
  return convertToString(grid, '\r\n');
}


function test() {
  // Prints representation of datagrid - 0's are black and 1's are white
  // Note: prettyPrint() only works properly if your interpreter returns a
  // representation of the datagrid in the correct format
  function prettyPrint(datagrid) {
    var consoleOutput = "<pre>", copy = datagrid.split("\r\n");
    for (let i = 0; i < copy.length; i++) {
      for (let j = 0; j < copy[i].length; j++) {
        consoleOutput += `<span style="color:${copy[i][j] === "0" ? "black" : "white"};`
        consoleOutput += `background-color:${copy[i][j] === "0" ? "black" : "white"}">xx</span>`;
      }
      consoleOutput += "<br />";
    }
    consoleOutput += "</pre>";
    console.log(consoleOutput);
    return datagrid;
  }
  // Displays the grid your interpreter returns
  function displayActual(actual) {
    console.log("You returned:");
    return prettyPrint(actual);
  }
  // Displays the expected final state of datagrid
  function displayExpected(expected) {
    console.log("Expected final state of data grid:");
    return prettyPrint(expected);
  }

  function assert(condition, message) {
      if (!condition) {
          throw message || "Assertion failed";
      }
  }

  let expected;
  let msg;

  msg = "Your interpreter should initialize all cells in the datagrid to 0";
  expected = displayExpected("000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000");
  assert(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9) === expected, msg);

  msg = "Your interpreter should adhere to the number of iterations specified";
  expected = displayExpected("111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000");
  assert(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9) === expected, msg);

  msg = "Your interpreter should traverse the 2D datagrid correctly";
  expected = displayExpected("111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000");
  assert(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9) === expected, msg);

  msg = "Your interpreter should traverse the 2D datagrid correctly for all of the \"n\", \"e\", \"s\" and \"w\" commands";
  expected = displayExpected("111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000");
  assert(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9) === expected, msg);

  msg = "Your interpreter should terminate normally and return a representation of the ";
  msg += "final state of the 2D datagrid when all commands have been considered from left ";
  msg += "to right even if the number of iterations specified have not been fully performed";
  expected = displayExpected("111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000");
  assert(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9) === expected, msg);
}


test();

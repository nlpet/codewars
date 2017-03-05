/*
  Simple Fun #176: Reverse Letter.

  Task

  Given a string str, reverse it omitting all non-alphabetic characters.
  Example

  For str = "krishan", the output should be "nahsirk".

  For str = "ultr53o?n", the output should be "nortlu".
  Input/Output

  [input] string str

  A string consists of lowercase latin letters, digits and symbols.
  [output] a string
*/


function reverseStr(s) {
  const rev = [];
  for (let i = s.length - 1; i >= 0; i--)
    rev.push(s[i]);
  return rev.join('');
}

function reverseLetter(str) {
  return reverseStr(str.replace(/[\W0-9_?]+/g,''));
}

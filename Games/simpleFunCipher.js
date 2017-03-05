/*
  Simple Fun #49: Decipher.

  Task

  Consider the following ciphering algorithm:

  For each character replace it with its code.
  Concatenate all of the obtained numbers.
  Given a ciphered string, return the initial one if it is known that it
  consists only of lowercase letters.

  Note: here the character's code means its decimal ASCII code, the numerical
  representation of a character used by most modern programming languages.
  Example

  For cipher = "10197115121", the output should be "easy".

  Explanation:

  charCode('e') = 101,
  charCode('a') = 97,
  charCode('s') = 115
  charCode('y') = 121.
*/

function decipher(cipher) {
  const plaintext = [],
  const ls = cipher.length;
  let i = 0;
  let lch, charCodeInt;

  while(i < ls) {
    if (cipher[i] == '1') { lch = 3; }
    else { lch = 2; }

    charCodeInt = parseInt(cipher.slice(i, i + lch));
    plaintext.push(String.fromCharCode(charCodeInt));
    i += lch;
  }

  return plaintext.join('');
}


function decipher(cipher) {
  return String.fromCharCode(...cipher.match(/1?\d\d/g))
}

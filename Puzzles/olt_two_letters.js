/*
TASK:
Convert two letters to their ASCII code(number format) and
your code should in one line and less than 54 characters.
*/


toASCIINumber=(a,b)=>+(''+a.charCodeAt(0)+b.charCodeAt(0))
toASCIINumber=(a,b)=>+Buffer.from(a+b).join``

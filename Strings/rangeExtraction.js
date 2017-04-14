

function assert(condition, message) {
    if (!condition) {
        throw message || "Assertion failed";
    } else {
      console.log(message + ' - OK');
    }
}

function updateResults(currentRange, result) {
  if (currentRange.end !== null) {
    if (currentRange.end - currentRange.start > 1) {
        result.push( `${currentRange.start}-${currentRange.end}` );
    } else {
        result.push( `${currentRange.start}`);
        result.push( `${currentRange.end}`);
    }

  } else {
    result.push( `${currentRange.start}`);
  }
}


function solution(list){
 const result = [];
 const currentRange = {start: null, end: null};

 list.forEach( (n, i) => {
   if (currentRange.start === null) { currentRange.start = n; }
   else if (n - currentRange.start === 1 || n - currentRange.end === 1) {
     currentRange.end = n;
     if (i === list.length - 1) {
       updateResults(currentRange, result);
     }
   } else {
     updateResults(currentRange, result);

     currentRange.start = n;
     currentRange.end = null;
   }
 });

 return result.join(',');
}


function test() {
  let result, msg;

  result = solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
  msg = `Expected ${result} to equal "-6,-3-1,3-5,7-11,14,15,17-20"`;
  assert(result === "-6,-3-1,3-5,7-11,14,15,17-20", msg);

}


test();

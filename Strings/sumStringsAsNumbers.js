
const zip= rows=>rows[0].map((_,c)=>rows.map(row=>row[c]))


function sumStrings(a,b) {
    const arrA = a.split('').reverse();
    const arrB = b.split('').reverse();
    const result = [];
    let rem = 0;
    let arr;

    zip([arrA, arrB]).forEach( ([n, m]) => {
      if(n && m) {
        let sm = parseInt(n) + parseInt(m);
        if (sm + rem > 9) {
          result.push((sm + rem) % 10);
          rem = Math.floor((sm + rem) / 10);
        } else {
          result.push(sm + rem);
          rem = 0;
        }
      }
    });

    if (arrA.length > arrB.length) {
      arr = arrA.slice(arrB.length);
    } else {
      arr = arrB.slice(arrA.length);
    }

    arr.map(n => parseInt(n)).forEach(n => {
      if (n + rem > 9) {
        rem = Math.floor((n + rem) / 10);
        result.push((n + rem) % 10);
      } else {
        result.push(n + rem);
        rem = 0;
      }
    });

    if (rem > 0) result.push(rem);
    return result.reverse().join('').replace(/^0+/, '');

}


// var a = '712569312664357328695151392'
// var b = '8100824045303269669937'
// expected = '712577413488402631964821329'

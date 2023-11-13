#!/usr/bin/node

function secondBiggest (arg) {
  if (arg.length <= 3) {
    return (0);
  } else {
    const array = arg.slice(2).map(Number);
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}
console.log(secondBiggest(process.argv));

#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  const a = Number(process.argv[2]);
  for (let i = 0; i < a; i += 1) {
    console.log('C is fun');
  }
}

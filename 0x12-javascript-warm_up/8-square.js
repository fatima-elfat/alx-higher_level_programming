#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
} else {
  const a = Number(process.argv[2]);
  for (let i = 0; i < a; i += 1) {
    console.log('X'.repeat(size));
  }
}

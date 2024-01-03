#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const towrite = process.argv[3];
fs.writeFile(filename, towrite, 'utf8', (error) => {
  if (error) console.log(error);
});

#!/usr/bin/node

const filesys = require('fs');

const filesys1 = filesys.readFileSync(process.argv[2], 'utf8');
const filesys2 = filesys.readFileSync(process.argv[3], 'utf8');
filesys.writeFileSync(process.argv[4], filesys1 + filesys2);

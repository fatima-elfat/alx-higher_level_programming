#!/usr/bin/node

cont filesys = require('fs');

cont filesys1 = filesys.readFileSync(process.argv[2], 'utf8');
cont filesys2 = filesys.readFileSync(process.argv[3], 'utf8');
filesys.writeFileSync(process.argv[4], filesys1 + filesys2);

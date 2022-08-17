#!/usr/bin/node
const fs = require('fs');
const strr = process.argv[3];

fs.writeFile(process.argv[2], strr, err => {
  if (err) {
    console.log(err);
  }
});

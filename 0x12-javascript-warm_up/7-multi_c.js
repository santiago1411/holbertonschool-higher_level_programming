#!/usr/bin/node
const vari = parseInt(process.argv[2]);

if (vari) {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

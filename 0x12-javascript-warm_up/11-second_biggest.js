#!/usr/bin/node
array = array.map(Number);
array = [... new Set(array)];
array = array.sort((a, b) => {return b - a});
console.log(array[1]);

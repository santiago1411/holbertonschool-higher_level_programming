#!/usr/bin/node
const var1 = parseInt(process.argv[2]);

function factorial (var1) {
  if (var1 <= 1 || isNaN(var1)) {
    return 1;
  } else {
    return var1 * factorial(var1 - 1);
  }
}
console.log(factorial(var1));

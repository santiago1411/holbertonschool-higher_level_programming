#!/usr/bin/node
const args = process.argv;
function compareNumbers (a, b) {
  return b - a;
}
if (args.length <= 3) {
  console.log(0);
} else {
  const numbers = args.slice(2).map((number) => {
    return parseInt(number);
  });
  numbers.sort(compareNumbers);
  console.log(numbers[1]);
}

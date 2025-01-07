// Program for factorial of a number

let factorial: number = 1;
let inputNumber: number = -13;

if (inputNumber < 0) {
  console.log("Factorial of negative number is not defined!");
} else {
  for (let i: number = inputNumber; i > 0; i--) {
    factorial = factorial * i;
  }
  console.log("Factorial of given number is "+factorial);
}

// 1. Write a JavaScript function to calculate the sum of two numbers. 

let sum = (a, b) => a + b ;
console.log(sum(5,5))

//2 Write a JavaScript program to find the maximum/largest number in an array.
var arr = [8, 4, 6, 2, 9, 13, 1, 6]
//var arr = []
var largest = arr[0]
if(arr.length === 0){
    console.log("Array is Empty!")
} else{
    for(let i = 1; i < arr.length; i++){
        if(largest < arr[i]){
            largest = arr[i];
        }
    }
    console.log(largest);
}
console.log(Math.max(...arr))

var lar = arr.reduce((max, num) => num > max ? num : max , arr[0])
console.log(lar)

//3 Write a JavaScript function to check if a given string is a palindrome (reads the same forwards and backwards). 

var str = "Malayalam"
str = str.toLowerCase();
var revStr = str.split("").reverse().join("");
if(str === revStr){
    console.log("Given String is Palindrome")
} else{
    console.log("Given string is not palindrome")
}

//4 Write a JavaScript function that takes an array of numbers and returns a new array with only the even numbers. 
var arr = [8, 4, 6, 2, 9, 13, 1, 6]

function findEven(arr){
   return arr.filter(num => num%2 ===0) 
}
console.log(findEven(arr.sort()))

//5. Write a JavaScript program to calculate the factorial of a given number. 
var num = 5
var factorial = 1
if(num < 0){
    console.log("Factorial of negative number is Undefined")
} else{
    for(let i = num; i > 0; i--){
        factorial *= i
    }
    console.log(factorial)
}

//6. Write a JavaScript function to check if a given number is prime. 

function isPrime(num){
    if(num <= 1) return false;
    for(let i = 2; i <= Math.sqrt(num); i++){
        if(num % i === 0) return false
    }
    return true;
}
console.log(isPrime(11))
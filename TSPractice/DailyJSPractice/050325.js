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

//7. Write a JavaScript program to find the largest element in a nested array. 

const nestedArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, [12, 13], 14]
];

function findLargest(nestArr){
    let larg = nestArr[0][0]
    for(let arr of nestArr){
        for(let ele of arr){
            if(ele > larg){
                larg = ele;
            }
        }
    }
    return largest;
}

console.log(findLargest(nestedArray))

//8. Write a JavaScript function that returns the Fibonacci sequence up to a given number of terms. 

function fibonacci(n){
    var a = 1;
    var b = 1;
    var fib = [];
    if(n <= 0) return [];
    if(n === 1){
        return [1];
    }if(n === 2) {
        return [a, b];
    } else{
        fib[0] = a;
        fib[1] = b;
        for(let i = 2; i < n; i++){
            fib[i] = a + b;
            a = b;
            b = fib[i];
        }
    }
    return fib;
}

console.log(fibonacci(10));

//9. Implement a function to reverse a string without using the built-in reverse() method. 
function rev(str){
    let reverse = []
    for(let i = 0 ; i < str.length ;i++){
        reverse.unshift(str[i])
    }
    return reverse.join("")
}
console.log(rev("Midhun"))

//10. Write a function that determines if two strings are anagrams of each other  
function checkAnagram(srt1, str2){
    return srt1.toLowerCase().split("").sort().join("") === str2.toLowerCase().split("").sort().join("")
}
console.log(checkAnagram("Listen", "Silent"))

//11. Given an array of numbers, write a function to find the largest and smallest numbers in the array. 

function largAndShort(arr){
    arr = arr.sort((a, b) => a - b)
    let largest = arr[arr.length - 1]
    let smallest = arr[0]
    return {largest, smallest}
}

console.log(largAndShort([6, 8, 13, 1, 7]))

//12. Write a function that takes an array of integers as input and returns a new array with only the unique elements. 
function getUnique(arr){
    let s = new Set(arr)
    let newArr = [...s]
    return newArr
}
console.log(getUnique([6, 8, 6, 7, 13, 1, 7]))

//13. Given a string, write a function to count the occurrences of each character in the string. 

function countOccurrence(str){
    let result = {}
    str = str.toLowerCase();
    for(let ele of str){
        result[ele] = (result[ele] || 0) + 1
    }
    return result
}
console.log(countOccurrence("Bobby"))

//14. Implement a function to remove duplicates from an array. 

function removeDuplicate(arr){
    let s = new Set(arr);
    let newArr = [...s]
    return newArr
}
console.log(removeDuplicate([6, 8, 6, 7, 13, 1, 7]))

//15. Write a function that takes an array of integers and returns the largest difference between any two numbers in the array. 
function largestDiff(arr){
    if(arr.length === 1) return arr[0];
    arr = arr.sort((a,b)=> a-b);
    let largestDiff = arr[arr.length - 1] - arr[0];
    return largestDiff
}
console.log(largestDiff([6]))
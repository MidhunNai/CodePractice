/*
Write a function expect that helps developers test their code. It should take in any value val and return an object with the following two functions.

toBe(val) accepts another value and returns true if the two values === each other. If they are not equal, it should throw an error "Not Equal".
notToBe(val) accepts another value and returns true if the two values !== each other. If they are equal, it should throw an error "Equal".
*/

function expect(val){
    return {
        toBe : function(expected){
            if(val !== expected){
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe : function(expected){
            if(val === expected){
                throw new Error("Equal");
            }
            return true;
        }
    }
}

// console.log(expect('5').toBe(5));

/*
Write a function createCounter. It should accept an initial integer in it. It should return an object with three functions.

The three functions are:

increment() increases the current value by 1 and then returns it.
decrement() reduces the current value by 1 and then returns it.
reset() sets the current value to init and then returns it.
*/

function createCounter(val){
    if (typeof init !== "number" || !Number.isInteger(init)) {
        throw new Error("Invalid input: Only integers are allowed.");
    }

    let current = init; // ✅ Correct: Maintain state separately

    return {
        increment: function () {
            return ++current;
        },
        decrement: function () {
            return --current;
        },
        reset: function () {
            current = init; // ✅ Reset works correctly
            return current;
        }
    };
}

//console.log(createCounter(5).increment());
//console.log(createCounter(5).decrement());
//console.log(createCounter(5).reset());
//console.log(createCounter('10').increment());

/*

Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

The returned array should be created such that returnedArray[i] = fn(arr[i], i).

Please solve it without the built-in Array.map method.

Example 1:

Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
Output: [2,3,4]
Explanation:
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 
Example 2:

Input: arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
Output: [1,3,5]
Explanation: The function increases each value by the index it resides in.
Example 3:

Input: arr = [10,20,30], fn = function constant() { return 42; }
Output: [42,42,42]
Explanation: The function always returns 42.
*/

function map(arr, fn){
    let result = [];
    for(let i = 0; i < arr.length ; i++){
        result.push(fn(arr[i], i));
    }
    return result;
}

// const plusone = function(n) { return n + 1; };
// console.log(map([1, 2, 3], plusone));

// const plusI = function(n, i) { return n + i; };
// console.log(map([1, 2, 3], plusI));
// const constant = function() { return 42; };
// console.log(map([10, 20, 30], constant));

/*
Given an integer array arr and a filtering function fn, return a filtered array filteredArr.

The fn function takes one or two arguments:

arr[i] - number from the arr
i - index of arr[i]
filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.

Please solve it without the built-in Array.filter method.
*/

function filter(arr, fn){
    let result = [];
    for(let i = 0; i < arr.length; i++){
        if(fn(arr[i], i)){
            result.push(arr[i]);
        }
    }
    return result;
}

// let newArr = [0,10,20,30]
// let greaterThan10 = function(n) { return n > 10; }
// console.log(filter(newArr, greaterThan10))
// newArr = [1,2,3];
// let firstIndex = function(n, i) { return i === 0; }
// console.log(filter(newArr, firstIndex))
// newArr = [-2,-1,0,1,2];
// let plusOne = function plusOne(n) { return n + 1 }
// console.log(filter(newArr, plusOne))

/*
Given an integer array nums, a reducer function fn, and an initial value init, return the final result obtained by executing the fn function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations: val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ... until every element in the array has been processed. The ultimate value of val is then returned.

If the length of the array is 0, the function should return init.

Please solve it without using the built-in Array.reduce method.
*/

function reduce(arr, fn, init){
    let result = init;
    if(arr.length === 0) return init;
    for(let i = 0; i < arr.length; i++){
        result = fn(result, arr[i]);
    }
    return result;
}
let nums = [1,2,3,4]
let sum = function(accum, curr) { return accum + curr; }
init = 0
console.log(reduce(nums, sum, init))
nums = [1,2,3,4]
sum = function(accum, curr) { return accum + curr * curr; }
init = 100
console.log(reduce(nums, sum, init))
nums = []
sum = function(accum, curr) { return 0; }
init = 25
console.log(reduce(nums, sum, init))
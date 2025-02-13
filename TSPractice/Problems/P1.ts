/*
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].
*/


function subArray(arr : number[], target : number) : number[]{
    let startingIndex = 0;
    let sum = 0;
    for(let endingIndex = 0; endingIndex < arr.length; endingIndex++){
        sum += arr[endingIndex];
        while(sum > target && startingIndex <= endingIndex){
            sum -= arr[startingIndex];
            startingIndex ++;
        }
        if(sum === target){
            return[startingIndex + 1 , endingIndex + 1]
        }
    }
    return [-1]
}

let arr = [1, 2, 3, 5, 7, 15];
let target = 12;

console.log(subArray(arr, target));
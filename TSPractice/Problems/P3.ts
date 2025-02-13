/*
Given an integer array arr[]. You need to find the maximum sum of a subarray.
*/

function maxSum(arr: number[]): number{
    let currentSum = 0;
    let maxSum = -Infinity;
    for(let num of arr){
        currentSum += num;
        maxSum = Math.max(currentSum, maxSum);
        if(currentSum < 0) currentSum = 0;
    }
    return maxSum;
}

export let arr = [2, 3, -8, 7, -1, 2, 3];
console.log(maxSum(arr));
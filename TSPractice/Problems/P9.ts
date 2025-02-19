/*
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
*/

function getMinDiff(arr: number[], k: number): number{
    let N = arr.length;
    if(N === 1) return 0;
    // Sprt the given array
    arr.sort((a, b) => a - b);
    // initial diff
    let initialDiff = arr[N-1] - arr[0]; // 9
    // Adjust the height
    let minHeight = arr[0] + k; //3
    let maxHeight = arr[N-1] - k; //8
    let minDiff = initialDiff; //9

    for(let i = 0; i < N-1; i++){
        let newMin = Math.min(minHeight, arr[i + 1] - k);
        let newMax = Math.max(maxHeight, arr[i] + k);

        if(newMin < 0) continue;
        minDiff = Math.min(minDiff, newMax - newMin);
    }
    return minDiff;
}

let k = 2
export let arr = [3, 9, 12, 16, 20];
console.log(getMinDiff(arr, k));
/*
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump 1 step, 2 steps, or 3 steps forward from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.
*/

export let arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9];

function jumpToEnd(arr: number[]): number{
    if(arr.length <= 1) return 0;
    if(arr[0] === 0) return -1;
    let jump = 0;
    let currentEnd = 0;
    let farthest = 0;
    for(let i = 0; i < arr.length - 1; i++){
        farthest = Math.max(farthest, i + arr[i]);
        if(i === currentEnd){
            jump++;
            currentEnd = farthest;
            if(currentEnd >= arr.length - 1) return jump;
        }
    }
    return -1;
}
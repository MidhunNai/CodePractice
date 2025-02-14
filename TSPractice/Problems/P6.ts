/*
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
*/


function findLeader(arr: number[]): number[]{
    let leader :number[] = [];
    let maxRight = -Infinity;

    for(let i = arr.length-1; i >= 0; i--){
        if(arr[i] >= maxRight){
            leader.push(arr[i]);
            maxRight = arr[i];
        }
    }

    return leader.reverse();
}

export let arr = [30, 10, 10, 5];
console.log(findLeader(arr));
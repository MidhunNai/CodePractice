/*
Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.
*/


function findDuplicate(arr: number[]): number[]{
    let duplicate: number[] = [];
    let frequency: Map<number, number> = new Map();
    for(let num of arr){
        frequency.set(num, (frequency.get(num) || 0) + 1);
    }
    for(let [num, count] of frequency){
        if(count > 1){
            duplicate.push(num);
        }
    }
    return duplicate;
}

export let arr = [2, 3, 1, 2, 3];
console.log(findDuplicate(arr));
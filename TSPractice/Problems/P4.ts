/*
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
*/

function findSecLargest(arr: number[]): number{
    arr = arr.sort((a, b) => a - b);
    let largestNumber = arr[0];
    let secondLargestNumber = 0;
    for(let num of arr){
        if(largestNumber < num){
            secondLargestNumber = largestNumber;
            largestNumber = num;
        }
    }
    if(secondLargestNumber === 0) return -1;
    return secondLargestNumber;
}

export let arr = [10, 10, 10];
console.log(findSecLargest(arr));
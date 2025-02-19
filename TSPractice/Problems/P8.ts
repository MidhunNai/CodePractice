/*
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.
*/

function kthSmallest(arr: number[], target: number): number{
    let swapped: boolean;
    do{
        swapped = false;
        for(let i = 0; i < arr.length - 1; i++){
            if(arr[i]>arr[i+1]){
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
    console.log(arr);
    return arr[target-1];
}

export let arr =  [2, 3, 1, 20, 15];
export let target = 4;
console.log(kthSmallest(arr, target));
/*
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
*/


function findMissingNum(arr : number[]) : number{
    arr = arr.sort((a, b) => a - b);
    console.log(arr);
    let missingNum = 0;
    let i = 0
    if(arr[0] != 1){
        return 1;
    } else{
        for(let num of arr){
            console.log('i is', i)
            console.log('Num is ', num)
            if((num+1) != arr[i+1]){
                missingNum = num+1
                console.log(missingNum);
                break;
            }
            i++;
        }
        return missingNum;
    }
}
export let arr = [13, 5, 4, 10, 7, 11, 1, 9, 12, 8, 2, 6];
console.log(findMissingNum(arr));
//--------------------------------------->>Correct Approach<<---------------------------------\\

/*
1. Get no. of elements, if n is total element of given array and 1 element is missing then no. of element must be n+1.
2. Get sum of n+1 elements.
3. Get sum of all the element given in the array
4. subtract sum of n+1 element and sum of given element which will give the missing number.
*/

function findMissingNumber(arr: number[]): number {
    let n = arr.length + 1;
    let sumN = (n * (n + 1)) / 2;
    let sumArr = arr.reduce((sum, num) => sum + num, 0);
    return sumN - sumArr;    
}
console.log(findMissingNumber(arr));
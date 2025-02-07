//Find largest numbe
function largestNumber(arr){
    let largestNumber = -Infinity;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > largestNumber){
            largestNumber = arr[i];
        }
    }
    return largestNumber === -Infinity ? null : largestNumber;
}

//Find second largest num,ber from array
function secondLargest(arr){
    if(arr.length < 2) return null;

    let largest = -Infinity;
    let secLargest = -Infinity;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > largest){
            secLargest = largest;
            largest = arr[i];
        } else if (arr[i] > secondLargest && arr[i] !== largest){
            secLargest = arr[i];
        }
    }
    return secLargest === -Infinity ? null : secLargest;
}

//Find Nth largest number
function findNthLargest(arr, N){
    let nthLargestNumber;
    arr = arr.sort((a,b) => a -b);
    nthLargestNumber = arr[arr.length - N];
    return nthLargestNumber;
}

let data = [2, 8, 67, 53, 11, 19, 94];
console.log(largestNumber(data));
console.log(secondLargest(data));
console.log(findNthLargest(data, 3));
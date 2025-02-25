let arr = [1, 2, 3, 4, 5, 5];
let arr2 = [2, 11, 49, 5]
console.log(arr.reverse());

if(arr.includes(4)){
     console.log(`Given array inclued 4`);
}

let sum = arr.reduce((a,b)=> a+b);
console.log(sum);

let words = ["cat", "apple", "bat"]
words.sort();
console.log(words);

let s = new Set(arr);
let arr1 = [...s];
console.log(arr1);

let duplicates = []
for(let ele of arr){
    if(arr2.includes(ele)){
        duplicates.push(ele);
    }
}
console.log(duplicates)

let dupli = [];
for(let i in arr){
    for (let j in arr){
        if(i != j && arr[i] === arr[j] && !dupli.includes(arr[i])){
            dupli.push(arr[i]);
        }
    }
}
console.log(dupli);

// arr2.sort((a, b) => a - b);


console.log(arr2)
let swapped = true;
do{
    swapped = false;
    for(let i = 0; i <  arr2.length; i++){
        if(arr2[i] > arr2[i+1]){
            let temp = arr2[i];
            arr2[i] = arr2[i + 1];
            arr2[i+1] = temp
            swapped = true;
        }
    }
} while(swapped);

console.log(arr2)

// Given arrays
let a1 = [10, 20, 30, 40];
let a2 = [30, 40, 50, 70];

let se = new Set([...a1, ...a2]);
let a = [...se];
console.log(a);

let count = arr.reduce((acc, curr) => {
    acc[curr] = (acc[curr] || 0) + 1;
    return acc;
}, {});
console.log(count);

let n = 3;
let set = new Set([...arr]);
let newArr = [...set];
newArr.sort((a,b)=>a-b);
nthLargest = newArr[(newArr.length)-n];
console.log(nthLargest)

// Find most frequently occurig element in the given arr

function mostFreqEle(arr){
    const count = arr.reduce((acc, curr)=>{
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {});
    return Object.keys(count).reduce((a, b) => (count[a]>count[b]?a:b));
}
console.log(mostFreqEle(arr));
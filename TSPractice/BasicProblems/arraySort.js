let arrayString = ["banana", "pineapple", "jackfruite", "apple"];
let arrayNum = [20, 8, 11, 49, 12];
console.log(arrayString.sort());
console.log(arrayNum.sort());
arrayString = ["banana", "pineapple", "jackfruite", "apple"];
arrayNum = [20, 8, 11, 49, 12];
console.log(arrayString)
console.log(arrayNum = arrayNum.sort((a, b)=> b - a));
arrayString = ["banana", "Pineapple", "jackfruite", "Apple"];
arrayString = arrayString.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
console.log(arrayString);

//Bubble Sort
arrayNum = [20, 8, 11, 49, 12];

function bubbleSort(arr) {
    let swapped;
    do{
        swapped = false;
        for(let i = 0; i < arr.length -1; i++) {
            if(arr[i] > arr[i+1]) {
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
}
bubbleSort(arrayNum)
console.log(arrayNum);


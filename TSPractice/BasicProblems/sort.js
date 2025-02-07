let arr1 = ["midhun", "bobby", "pankaj", "durgesh"];
console.log(arr1.sort());
let arr2 = [3, 1, 4, 7, 20];
console.log(arr2.sort((a, b) => a - b));

function bubbleSort(arr){
    let swapped;
    do{
        swapped = false;
        for(let i = 0; i < arr.length; i++){
            if(arr[i]>arr[i+1]){
                let temp = arr[i];
                arr[1] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
    } while(swapped)
        return arr;
}
console.log(bubbleSort(arr2));
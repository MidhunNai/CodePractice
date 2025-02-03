let arr = [1, 5, 7, 10, 15];
arr.unshift(11);
let removedElement = arr.pop();
console.log(removedElement, arr);
console.log(arr.reverse());
arr = [];
console.log(arr);
arr = ["Midhun", "Molly", "Vimi", "Vijayan"];
console.log(arr.includes("Molly"));
let arr1 = [1, 8, 20, 11];
arr1.unshift(28);
arr1.push(12);
arr1.splice(2, 0, 18);
console.log(arr1);
//Sum of all element of array
let array = [11, 12, 20, 28];
let arraySum = array.reduce((sum, arrayElement) => sum + arrayElement, 0);
console.log(arraySum);
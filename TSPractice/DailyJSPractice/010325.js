// Extract value of a property as array from an array of objects
let input = [
    { id: 1, name: 'Alice', age: 25 },
    { id: 2, name: 'Bob', age: 30 },
    { id: 3, name: 'Charlie', age: 35 }
  ];

function objProArr(arr) {
  let newArr = arr.map((prop) => prop.name);
  return newArr;
}
console.log(objProArr(input));

//Split an Array into Chunks
let a = [ 10, 20, 30, 40, 50, 60, 70]
let chunk = 4

let a1 = a.slice(0, chunk)
let a2 = a.slice(chunk, chunk + a.length)
console.log(a1, a2)

//Convert Comma Separated String To Array
const s = "apple,banana,cherry";
let sArray = s.split(",")
console.log(sArray)

//Copy Array Items Into Another Array in JavaScript
let b = [1, 2, 3, 4, 5]
let b1 = [...b]
console.log(b1)

//Program to find non unique value in array
let c = [1, 2, 3, 4, 5, 2, 5]
let c1 = c.filter((value) =>{
  return c.indexOf(value) === c.lastIndexOf(value);
});
console.log(c1)

// Explain closure with example - In js if an function is called within another function it can remember the variables initialized on outer function

function createCounter(n){
  return function(){
    return n++;
  }
}

const counter = createCounter(5)
console.log(counter);
console.log(counter());
console.log(counter());
console.log(counter());

// function findDuplicates(arr){
//     let seen = new Set();
//     return arr.filter(item => seen.has(item) ? true : !seen.add(item));
// }

// let givenArray = [1, 2, 3, 4, 2, 3, 5, 1];
// let duplicateValues = findDuplicates(givenArray);
// console.log(duplicateValues);

// let a = [ 10, 20, 20, 30, 40, 50, 50 ];
// let s = new Set(a);
// let a1 = [...s];
// console.log(a1);

let a1 = [10, 20, 30, 40];
let a2 = [30, 40, 50, 70];

let s = new Set([...a1, ...a2]);
let newArray = [...s];
console.log(newArray);

let friends = [
    {name: "midhun", age: 30},
    {name: "brajesh", age: 31},
    {name: "pankaj", age: 30},
    {name: "durgesh", age: 30}
];
friends.sort((a, b) => a.name.localeCompare(b.name));
console.log(friends)
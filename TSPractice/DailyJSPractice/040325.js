let arr = [11,23,34,23,56,48,23,56,11]
let s = new Set(arr)
let newArr = [...s]
console.log(newArr)
newArr.sort((a, b) => b - a)
console.log(newArr)
//Program to swap two number

function swapNumber( a: number, b: number) : [number, number] {
    let temp = a;
    a = b;
    b = temp;
    return [a, b];
}

let a: number = 5;
let b: number = 10;
[a, b] = swapNumber(a, b);

console.log(a, b);
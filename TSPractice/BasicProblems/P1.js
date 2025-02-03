// Program for Fibonacci series up to n

function fibonacci(n) {
    let fibSeries = [];
    let a = 0, b = 1;
    for(let i = 0; i < n; i++) {
        fibSeries.push(a);
        let next = a + b;
        a = b;
        b = next;
    }
    return fibSeries;
}

let num = 10;
const result = fibonacci(num);
console.log(result);


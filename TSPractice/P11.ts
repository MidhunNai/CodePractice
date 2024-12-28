// Program to Find Sum of Fibonacci Series Numbers of First N Even Indexes

export let n = 5;
export let a = 0;
export let b = 1;
export let evenCount = 0;
export let index = 0;
export let sum = 0;

while(evenCount < n) {
    if(index % 2 ===0) {
        sum += a;
        evenCount++;
    }
    let next = a + b;
    a = b;
    b = next;
    index++;
}
console.log("Sum of even index of N in Fibonacci number is "+ sum);
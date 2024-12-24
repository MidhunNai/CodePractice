//Program to Find LCM of Two Numbers - Option 1

export let a : number = 15;
export let b : number = 25;

export let largest : number = (a > b) ? a : b;

while(true) {
    if (largest % a === 0 && largest % b === 0) 
        break;
    largest++;
}

console.log(`LCM of ${a} and ${b} is ${largest}`);

//Program to Find LCM of Two Numbers - Option 2

export let c: number = 15;
export let d: number = 25;

// Helper function to calculate GCD using the Euclidean algorithm
const gcd = (x: number, y: number): number => {
    return y === 0 ? x : gcd(y, x % y);
};

// LCM formula
export let lcm: number = (c * d) / gcd(c, d);

console.log(`LCM of ${a} and ${b} is ${lcm}`);
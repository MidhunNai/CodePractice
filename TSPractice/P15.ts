// Program for compound interest

export let p = 1200;
export let t = 2;
export let r = 5.4;
export let ci = p * (Math.pow((1 + r/100), t));
console.log("The compound intrest of given principal amount is "+ ci);

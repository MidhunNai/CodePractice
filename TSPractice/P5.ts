//Find Largest Among 3 Numbers

function largestOfThree( a: number, b: number, c: number) : number {
    return  c > (a > b ? a : b) ? c : ((a > b) ? a : b) ;
}

let d : number = 5;
let e : number = 10;
let c : number = 8;
let largest = largestOfThree(d, e, c);
console.log("The largest number is "+largest);


// Program to Print Right Triangle Star Pattern

export let n = 5;
for(let i = 1; i <= n; i++){
    for(let j = 1; j <= i; j++){
        process.stdout.write("*");
    }
    console.log(" ");
}
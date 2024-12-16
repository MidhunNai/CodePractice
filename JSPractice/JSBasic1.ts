// Program to get input from user and print it

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter something: ', (input) => {
    console.log(`You entered: ${input}`);
    rl.close();
})
// Program to find the ASCII value of a character
function findAsciiValue(char: string): number {
    if (char.length !== 1) {
        throw new Error("Please provide a single character.");
    }
    return char.charCodeAt(0); // Get the ASCII value
}

// Example usage
const character = 'A'; // Replace with any character to test
const asciiValue = findAsciiValue(character);

console.log(`The ASCII value of '${character}' is ${asciiValue}.`);
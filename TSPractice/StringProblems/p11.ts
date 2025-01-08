//Program to Replace Characters of a String

export let s1 = "Hello world, welcome to Kerala.";
export let oldWord = "Hello";
export let newWord = "Hi";

export const replacedString = s1.split(" ").map(word => word === oldWord ? newWord : word).join(" ");
console.log(replacedString);
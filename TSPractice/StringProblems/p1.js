// Program to count words of a string

function countWords(words) {
    let count = 0;
    let wordsArray = words.split(" ");
    return wordsArray.length;
}

let words = "My name is Midhun Nair";
let totalCount = countWords(words);
console.log(totalCount);

// Program to revese a string

function reverseString(str){
    return reverseString = str.split('').reverse().join('');
}

function reverseWord(str){
    return reverseWord = str.split(" ").map(word=>word.split('').reverse().join('')).join(' ');
}
let str = 'My name is Midhun Nair'
console.log(str);
console.log(reverseString(str));
console.log(reverseWord(str));
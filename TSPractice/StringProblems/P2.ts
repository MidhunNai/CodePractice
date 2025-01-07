//Program to check if string contain any whitespace charecters

let str = "My name is midhun nair";
function checkWhiteSpace(str: string): boolean {
    let regex = /\s/;
    return regex.test(str);
}
let isWhiteSpace: boolean = checkWhiteSpace(str);
console.log("Does the string contain whitespaces? "+ isWhiteSpace);
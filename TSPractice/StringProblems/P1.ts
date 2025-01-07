// Program to count words of a string

const string1: string = "My name is Midhun Nair and I am an engineer.";
function countWords(str: string): number {
    if(!str.trim()) {
        return 0;
    }
    const words: string[] = str.trim().split(/\s+/);
    return words.length;
}
console.log("Number of words in the given string is " + countWords(string1));
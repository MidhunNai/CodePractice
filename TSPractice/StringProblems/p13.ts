//Get a Number of Vowels in a String

export let s1 = "Hello Midhun, welcome to Kerala.";

function countVowels(str: String): number {
    let vowelsCount = 0;
    for(let character of str.split("")){
        if(character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u') {
            vowelsCount++;
        }
    }
    return vowelsCount;
}

console.log(countVowels(s1));
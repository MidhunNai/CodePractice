// Program to revese a string

export let str = "Midhun";
function reverseString(str: String): String {
    return str.split('').reverse().join('');
}
console.log(reverseString(str));
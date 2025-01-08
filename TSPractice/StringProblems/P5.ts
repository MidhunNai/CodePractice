// Check if a String “StartsWith” Another String

export const s = "Hello world";
export const prefix = "Hello";
if(s.startsWith(prefix)){
    console.log(`The string starts with ${prefix}`);
} else {
    console.log(`The string does not start with ${prefix}`);
}
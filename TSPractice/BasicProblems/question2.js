let str = "My name is Midhun Nair";
let count = str.split(" ").length;
console.log(count);
console.log(str.includes(" "));
console.log(str.split("").reverse().join(""));
console.log(str.replace("My", "Your"));
if(str.startsWith("My")){
    console.log("The string starts with'My'");
}else{
    console.log("The string does not start with 'My'");
}

let strArray = str.split("");
let revArr = [];
for(let i = strArray.length-1; i>=0; i--){
    revArr.push(strArray[i]);
}
console.log(revArr.join(""));

console.log(str.slice(1));
console.log(str);
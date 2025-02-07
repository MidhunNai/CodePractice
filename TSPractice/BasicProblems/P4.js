const generateNumber = (start, end) => Array.from({length: end - start + 1}, (_ , i) => start + i);
const newArray = generateNumber(5, 15);
console.log(newArray);

function generateNumRange(start, end){
    let result = [];
    for(let i = start; i <= end; i++){
        result.push(start);
        start++;
    }
    return result;
}


const generateCharRange = (start, end) => 
    Array.from(
        { length: end.charCodeAt(0) - start.charCodeAt(0) + 1 }, 
        (_, i) => String.fromCharCode(start.charCodeAt(0) + i)
    );

const generatedArray = generateNumRange(5, 15);
console.log(generatedArray);
console.log(generateCharRange('a', 'm'));
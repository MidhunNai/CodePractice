//Frequency of characters Appearance

export let s1 = "Hello Midhun, Welcome to Kerala";
export let char1 = "a";
function getFrequency(char2: String) : number {
    let frequency = 0;
    for(let charecters of s1.split("")){
        if(charecters == char2){
            frequency++;
        }
    }
    return frequency;
}
console.log(getFrequency(char1));
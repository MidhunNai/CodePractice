//Program to Find if a Given Year is a Leap Year

let year = 2000;
let leapYear = false;
if(year % 4 === 0){
    if(year % 100 === 0){
        if(year % 400 === 0){
            leapYear = true;
        } else {
            leapYear = false;
        }
    } else {
        leapYear = true;
    }
}

if(leapYear) {
    console.log("Giver year is a leap year!")
} else {
    console.log("Giver year is not a leap year!")
}
// Program to Print Reverse Pyramid Star Pattern

/* 
*************
 ***********
  *********
   *******
    *****
     ***
      *
*/

export let n = 7;
for(let i = 0; i < n; i++) {
    let space = " ".repeat(i);
    let stars = "*".repeat((2*(n - i))-1);
    console.log(space + stars);
}
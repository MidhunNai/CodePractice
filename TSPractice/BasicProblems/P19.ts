// Program to Print Pyramid Number Pattern

export let n = 5;
for (let i = 1; i <= n; i++) {
    let row = "";
    for (let j = 1; j <= n-i; j++) {
        row += "  ";
    }
    for (let k = 0; k < i; k++) {
        row += (i + k) + " ";
    }
    for (let k = i - 2; k >= 0; k--) {
        row += (i + k) + " ";
    }
    console.log(row.trimEnd());
}
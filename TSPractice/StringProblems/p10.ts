// Compare two strings

export let s1 = "My name is Midhun Nair";
export let s2 = "Midhun Nair"

export let ans = s1.localeCompare(s2);
export let res = "";
if(ans == -1) {
    res = `${s1} comes before ${s2}`;
} else if(ans === 0) {
    res = "Both strings are same";
} else {
    res = `${s1} comes after ${s2}`;
}

console.log(res);
function removeDuplicate( arr ) {
    return [...new Set(arr)];
}

function sortNum(arr){
    return arr.sort((a, b) => a - b);
}

function hasCommonItems(arr1, arr2){
    return arr1.some(item => arr2.includes(item));
}

function findCommonItem(arr1, arr2) {
    const commonItems = arr1.filter(item => arr2.includes(item));
    return commonItems > 0 ? commonItems : "No common items!";
}

let nums = [12, 11, 19, 20, 94, 11, 19];
nums = removeDuplicate(nums);
nums = sortNum(nums);
console.log(nums);

const array1 = [1, 2, 3, 4];
const array2 = [5, 6, 3, 7];
console.log(hasCommonItems(array1, array2));
console.log(findCommonItem(array1, array2));

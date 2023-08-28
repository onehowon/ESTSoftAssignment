let arr1 = [1, 2, 3];
let arr2 = arr1;
console.log(arr2);

arr1[0] = 10;
// arr1 = [10, 20];
console.log(arr2);

// 비교해보세요.
let value1 = 10;
let value2 = value1;
console.log(value2);

value1 = 20;
console.log(value2);
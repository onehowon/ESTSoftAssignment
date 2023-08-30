const aespa = ["카리나", "윈터", "지젤", "닝닝"]
console.log(aespa);

const emoji = '♥';

const newArray = aespa.map(function(str){
    var lastChar = str.slice(-1);
    return str.slice(0, -1) + lastChar + emoji;
})

console.log(newArray);
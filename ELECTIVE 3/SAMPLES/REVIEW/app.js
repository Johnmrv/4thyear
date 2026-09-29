const fs = require('fs');
const path = require('path');
const calc = require('./calculator');

const  multResult = calc.multiply(4, 5);
const divResult = calc.divide(10, 2);

console.log(multResult);
console.log(divResult);

const content = `Multiply (4 * 5): ${multResult}\nDivide (10 / 2): ${divResult}`;

fs.writeFileSync('result.txt', multResult);



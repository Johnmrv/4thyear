const arrayOp = require('./calc');

const scores = [1, 2, 3, 4, 5];

console.log('Original');
console.log(scores);


arrayOp.addScore(scores, 6);
console.log('Other');
console.log(scores);

arrayOp.removeLastScore(scores);
console.log('Other');
console.log(scores);

arrayOp.removeFirstScore(scores);
console.log('Other hey');
console.log(scores);

const result = arrayOp.findScore(scores, 1);

if (result) {
    console.log('Has been found');
} else {
    console.log('not found');
}

console.log(scores);
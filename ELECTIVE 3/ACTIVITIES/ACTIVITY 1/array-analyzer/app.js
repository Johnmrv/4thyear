const arrayOperations = require('./modules/arrayOperations.js');
const statistics = require('./modules/statistics.js');

let scores = [85, 90, 78, 92, 74, 88, 95, 67, 80, 85];

console.log('Original Scores:');
console.log(scores);

arrayOperations.addScore(scores, 81);
console.log('\nAfter Adding 81:');
console.log(scores);

let removedScore = arrayOperations.removeLastScore(scores);
console.log('\nRemoved Score: ' + removedScore);
console.log('After Removing Last Score:');
console.log(scores);

console.log('\nFind Score 90: ' + arrayOperations.findScore(scores, 90));
console.log('Passing Scores:');
console.log(arrayOperations.filterPassing(scores));

console.log('\nAverage: ' + statistics.average(scores));
console.log('Highest Score: ' + statistics.highest(scores));
console.log('Lowest Score: ' + statistics.lowest(scores));
console.log('Passing Scores Count: ' + statistics.countPassing(scores));
console.log('Failing Scores Count: ' + statistics.countFailing(scores));
console.log('Sorted Scores:');
console.log(statistics.sortScores(scores));

console.log('\nGrade Conversion:');
console.log(statistics.gradeConversion(scores));

console.log('\nScore Frequency:');
let frequency = statistics.scoreFrequency(scores);
for(let score in frequency){
    console.log(score + ' = ' + frequency[score] + ' time/s');
}
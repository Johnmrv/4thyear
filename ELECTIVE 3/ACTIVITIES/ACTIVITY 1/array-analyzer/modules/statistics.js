module.exports.average = (scores)=> {
    let total = scores.reduce((sum, score) => sum + score, 0);
    return total / scores.length;
}

module.exports.highest = (scores)=> {
    return Math.max(...scores);
}

module.exports.lowest = (scores)=> {
    return Math.min(...scores);
}

module.exports.sortScores = (scores)=> {
    return [...scores].sort((a, b) => b - a);
}

module.exports.countPassing = (scores)=> {
    return scores.filter(score => score >= 75).length;
}

module.exports.countFailing = (scores)=> {
    return scores.filter(score => score < 75).length;
}

module.exports.gradeConversion = (scores)=> {
    return scores.map(score => {
        if(score >= 90){
            return score + ' = A';
        } else if(score >= 85){
            return score + ' = B+';
        } else if(score >= 80){
            return score + ' = B';
        } else if(score >= 75){
            return score + ' = C';
        } else{
            return score + ' = F';
        }
    });
}

module.exports.scoreFrequency = (scores)=> {
    let frequency = {};

    scores.forEach(score => {
        if(frequency[score]){
            frequency[score]++;
        } else{
            frequency[score] = 1;
        }
    });

    return frequency;
}

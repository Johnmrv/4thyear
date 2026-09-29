module.exports.addScore = (scores, score) => {
    scores.push(score);
    return scores;
}

module.exports.removeLastScore = (scores) => {
    return scores.pop();
}

module.exports.removeFirstScore = (scores) => {
    return scores.shift();
}

module.exports.findScore = (scores, score) =>{
    return scores.includes(score);
}

module.exports.filterPassing = (scores) => {
    return scores.filter(score => score >= 75);
}
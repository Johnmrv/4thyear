const path = require('path');

const filepath = path.join(__dirname, 'documents', 'report.pdf');

console.log('File information');

console.log('Fullpath: ', filepath);
console.log('Basename: ', path.basename(filepath));
console.log('Directory: ', path.dirname(filepath));
console.log('Extension: ', path.extname(filepath));
console.log('Filenam w/o extension: ', path.basename(filepath, path.extname(filepath)));
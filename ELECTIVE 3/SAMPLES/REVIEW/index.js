const fs = require('fs');
const path = require('path');

fs.writeFile('log.txt', 'Server started', (err)=>{

    if (err) throw err;

    fs.readFile('log.txt', 'utf8', (err, data)=>{
        if (err) throw err;
        console.log(data);
         
        const extName = path.extname('log.txt');
        console.log('Extension Name: ${extName}')


    });
})
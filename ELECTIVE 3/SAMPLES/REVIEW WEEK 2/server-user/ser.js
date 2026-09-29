const http = require('http');
const fs = require('fs');
const EventEmitter = require('events');

const serverEmitter =  new EventEmitter();

serverEmitter.on('serverAccess', (url) => {
    console.log(`[Server Access]: Route at ${url}`);
});

serverEmitter.on('logAccess', (message) => {
    const timestamp = new Date().toLocaleString();
    const logEntry = `${timestamp} - ${message}`;

    fs.appendFile('loger.text', logEntry, (err) => {
        if (err){
            console.error('error', err);
        }
    });
});

const server = http.createServer((req, res) => {
    serverEmitter.emit('serverAcces', req.url);
    serverEmitter.emit('logAccess', `User Request route ${req.url}`);

    if (req.method === 'GET' && req.url === '/') {
        res.statusCode = 200;
        res.setHeader('Content-type', 'text/plain');
        res.end('Homepage');
    } else if(req.method === 'GET' && req.url === "/user") {
        fs.readFile('user.json', 'utf8', (err, data) =>{
            if (err) {
               res.statusCode = 500;
        res.setHeader('Content-type', 'text/plain');
        res.end('error'); 
            }
            res.statusCode = 200;
        res.setHeader('Content-type', 'text/plain');
        res.end(data);
        });
    } else {
        res.statusCode = 400;
        res.setHeader('Content-type', 'text/plain');
        res.end('PAGE NOT FOUND');
    }


});

const PORT = 3000;

server.listen(PORT, ()=>{
    console.log(`server running at http://localhost:${PORT}/`);

});
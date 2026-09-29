const http = require('http');
const fs = require('fs');
const EventEmitter = require('events');

const serverEmitter = new EventEmitter();

serverEmitter.on('serverAccess', (url) => {
    console.log(`[Server Access]: Route at ${url}`);
});

serverEmitter.on('logAccess', (message) =>{
    const timestamp = new Date().toLocaleString();
    const logEntry = `[${timestamp}] - ${message}\n`;

    fs.appendFile('server2ss-log.txt', logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
});

// serverEmitter.on('logAccess', (message) => {
//     const timestamp = new Date().toLocaleString();
//     const logEntry = `[${timestamp}] - ${message}\n`;

//     fs.appendFile('norew.txt', logEntry, (err) =>{
//         if (err) {
//             console.error('error', err);
//         }
//     });
// });

const server = http.createServer((req,res) => {
    serverEmitter.emit('serverAccess', req.url);
    serverEmitter.emit('logAccess', `User Requested route ${req.url}`);


    if (req.method === 'GET' && req.url === '/'){
        res.statusCode = 200;
        res.setHeader('Content-type', 'text/type');
        res.end('Welcome to Homepage');
    } 
    else if (req.method === 'GET' && req.url === '/user'){
        fs.readFile('user.json', 'utf8', (err, data) => {
            if(err){
                res.statusCode = 500;
                res.setHeader('Content-type', 'text/plain');
                res.end('Welcome to erro');
            }

        res.statusCode = 200;
        res.setHeader('Content-type', 'text/plain');
        res.end(data);
        });
    }
        if (req.method === 'GET' && req.url === '/page') {
    fs.readFile('index.html', 'utf8', (err, data) => {
        if (err) {
            res.statusCode = 500;
            res.setHeader('Content-Type', 'text/plain');
            return res.end('Server Error: Failed to load index.html');
        }

        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
        res.end(data);
    });
}
    else {
        res.statusCode = 400;
        res.setHeader('Content-type', 'text/plain');
        res.end('Invalid');
    }
    
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
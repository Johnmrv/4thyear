const http = require('http');
const fs = require('fs');
const EventEmitter = require('events');

const serv = new EventEmitter();

serv.on('ServAcc', (url)=>{
    console.log(`${url}`);
});

serv.on('logAcc',(message)=>{
const time = new Date().toLocaleString();
const login = `${time} - ${message}`;

fs.appendFile('logAcc', login,(err)=>{
    if(err){
        console.error('error',err);

    }
});
});


const server = http.createServer((req,res)=>{
    serv.emit('ServAcc',req.url);
    serv.emit('logAcc',req.url);

    if(req.method === 'GET' && req.url === '/'){
        res.statusCode=200;
        res.setHeader('Content-Type','text/plain');
        res.end('Hello bitch');
    }
    else if(req.method === 'GET' && req.url === '/user'){
        fs.readFile('user.json','utf8',(err,data)=>{
            if(err){
                  res.statusCode=500;
        res.setHeader('Content-Type','text/plain');
        res.end('error');
            }
res.statusCode=200;
        res.setHeader('Content-Type','text/plain');
        res.end(data);
        });
      
    }
});
const port = 300;
server.listen(port,()=>{
    console.log(`http://localhost:${port}/`);
});
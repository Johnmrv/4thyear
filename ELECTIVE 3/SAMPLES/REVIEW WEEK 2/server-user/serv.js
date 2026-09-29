const http = require('http');
const fs = require('fs');
const EventEmitter = require('events');

const serv = new EventEmitter();

serv.on('ServAccess', (url)=> {
    console.log(`[Serv Access]: Request -> ${url}`);
});
serv.on('loginAct', (message)=>{
    const time = new Date().toLocaleString();
    const log = `[${time}] - ${message}\n `;
    fs.appendFile('server_logss.txt', log , (err)=>
        {
            if(err){
            console.error('error',err);
            }
        });

});

const server = http.createServer((req,res)=>{
    serv.emit('ServAccess',req.url);
    serv.emit('loginAct',`User requat: ${req.url}`);

    if(req.method === 'GET' && req.url === '/'){
        res.statusCode = 200;
        res.setHeader('Content-type', 'text/plain');
        res.end('Welcome to homepage');
    } else if (req.method === 'GET' && req.url === '/user'){
        fs.readFile('user.json', 'utf8', (err, data) => {
            if (err){
            res.statusCode = 500;
            res.setHeader('Content-type', 'text/plain');
            res.end("errorr");
            }
            res.statusCode = 200;
            res.setHeader('Content-type', 'text/plain');
            res.end(data);
        });
    } else {
        res.statusCode = 400;
        res.setHeader('Content-type', 'text/plain');
        res.end('404 Error: Page not found');
    }
});

const PORT = 3000;
server.listen(PORT, () =>{
    console.log(`Server is currently running at http://localhost: ${PORT}/`);
});


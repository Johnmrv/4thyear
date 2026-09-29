
const http = require('http'); 
const fs = require('fs'); 
const EventEmitter = require('events'); 

const serverEmitter = new EventEmitter(); 

serverEmitter.on('serverAccess', (url) => {
  console.log(`[Server Access]: Request received for route -> ${url}`); 
});

serverEmitter.on('logActivity', (message) => {
  const timestamp = new Date().toLocaleString(); 
  const logEntry = `[${timestamp}]\n${message}\n`; 

  fs.appendFile('server-log.txt', logEntry, (err) => {
    if (err) {
      console.error('Error writing to log file:', err);
    }
  }); 
});


const server = http.createServer((req, res) => {
  serverEmitter.emit('serverAccess', req.url);
  serverEmitter.emit('logActivity', `User requested route: ${req.url}`);


  if (req.method === 'GET' && req.url === '/') {
    res.statusCode = 200; 
    res.setHeader('Content-Type', 'text/plain'); 
    res.end('Welcome to the Student Information Server'); 
  } 

  else if (req.method === 'GET' && req.url === '/students') {
    fs.readFile('students.json', 'utf8', (err, data) => {
      if (err) {
        res.statusCode = 500; 
        res.setHeader('Content-Type', 'text/plain');
        res.end('500 Internal Server Error'); 
        return;
      }
      res.statusCode = 200; 
      res.setHeader('Content-Type', 'application/json'); 
      res.end(data); 
    }); 
  } 

  else {
    res.statusCode = 404; 
    res.setHeader('Content-Type', 'text/plain'); 
    res.end('404 Error: Page Not Found'); 
  }
});

const PORT = 3000; 
server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}/`); 
});
const http = require('http');
const port = 3000;
const fs = require('fs');
const path = require('path');

console.log(__dirname);

const server = http.createServer((req, res) => {

    if (req.url === '/') {

        const filepath = path.join(__dirname, 'views', 'index.html');

        fs.readFile(filepath, (err, data) => {

            if (err) {
                console.log(err.message);

                res.statusCode = 500;
                res.setHeader('Content-Type', 'text/html');
                res.end('<strong>Error loading the page</strong>');

            } else {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/html');
                res.end(data);
            }

        });

    } else if (req.url === '/about') {

        const filepath = path.join(__dirname, 'views', 'about.html');

        fs.readFile(filepath, (err, data) => {

            if (err) {
                console.log(err.message);

                res.statusCode = 500;
                res.setHeader('Content-Type', 'text/html');
                res.end('<strong>Error loading the page</strong>');

            } else {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/html');
                res.end(data);
            }

        });
    } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/html');
        res.end('<strong>Page not found</strong>');

    }

});

server.listen(port, () => {
    console.log(`Server running at port: ${port}`);
});
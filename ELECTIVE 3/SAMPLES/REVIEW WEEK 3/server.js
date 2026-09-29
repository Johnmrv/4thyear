const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const cors = require('cors');
const morgan = require('morgan');
const { v4: uuidv4 } = require('uuid');
const chalk = require('chalk');

const app = express();
const PORT = 3000;
const dataFile = path.join(__dirname, 'data', 'students.json');


app.use(express.json());
app.use(cors());
app.use(morgan('dev'));

async function readStudents(){
    const data = await fs.readFile(dataFile, 'utf8');
    return JSON.parse(data);
}

async function writeStudents(students){
    await fs.writeFile(dataFile, JSON.stringify(students, null, 2));
}

function validateStudent(student){
    const{ name, course, year, email } = student;
    if(!name || !course || !email || year === undefined || year === '')
        return 'Name, course, year, and email are required.';
    if(!Number.isInteger(Number(year)) || Number(year) < 1 || Number(year) >6)
        return 'Year must be a number from 1 to 6.';
    return null; 
}

app.get('/', (req, res) => {
    res.status(200).json({
        message: 'Welcome to the Student Management API',
        endpoints: [
            'GET /api/students',
            'GET /api/students/:id',
            'POST /api/students',
            'PUT /api/students/:id',
            'DELETE /api/students/:id',
        ]
    });
});


app.get('/api/students', async (req, res)=>{
    try{
        res.status(200).json(await readStudents());
    } catch(error){
        res.status(500).json({error: 'Unable to read students data.'});
    }
});

app.get('/api/students/:id', async (req, res)=>{
    try{
        const students = await readStudents();
        const student = students.find(item => item.id === req.params.id);
        if (!student) return res.status(404).json({ error: 'Student not found. '});

        console.log(chalk.yellow(`Found student: ${student.name} (${student.id})`));
        res.status(200).json(student);

    } catch (error){
        res.status(500).json({error: 'Unable to read students data. '});
    }
});

app.post('/api/students', async (req,res)=>{
    const error = validateStudent(req.body);
    if (error) return res.status(400).json({ error });

    try {
        const students = await readStudents();
        const student = {
            id: uuidv4(),
            name: req.body.name,
            course: req.body.course,
            year: Number(req.body.year),
            email: req.body.email
        };
        students.push(student);
        await writeStudents(students);
        console.log(chalk.green(`Added student: ${student.name} (${student.id})`));
        res.status(201).json(student);
    } catch (err){
        res.status(500).json({ error: 'Unable to save student data. '});
    }

});

app.put('/api/students/:id', async (req, res) =>{
    const error = validateStudent(req.body);
    if (error) return res.status(400).json({error});


    try {
        const students = await readStudents();
        const index = students.findIndex(item => item.id === req.params.id);

        if (index === -1) return res.status(404).json({error: 'Student not found. '});

        students[index] = {
            ...students[index],
            name: req.body.name,
            course: req.body.course,
            year: Number(req.body.year),
            email: req.body.email,
        };
        await writeStudents(students);
        console.log(chalk.blue(`Updated student: ${students[index].name} (${students[index].id})`));
        res.status(200).json(students[index]);
    } catch (error){
        res.status(500).json({error: `Unable to update student data. `});
    }
});

app.delete('/api/student/:id', async (req, res) => {
    try {
        const students = await readStudents();
        const index = students.findIndex(item => item.id === req.params.id);
        if (index === -1) return res.status(404).json({ error: 'Student not found.'});

        const deletedStudent = students.splice(index, 1)[0];
        await writeStudents(students);
        console.log(chalk.red(`Deleted student: ${deletedStudent.name} (${deletedStudent.id})`));
        res.status(200).json({message: `Student deleted successfully.` , student: deletedStudent});
    } catch (err) {
        res.status(500).json({error: 'Unable to delete student data. '});
    }
});

app.use((req,res) => res.status(404).json({error: 'Route not found. '}));
app.listen(PORT, () => console.log(`Student API is running at http://localhost:${PORT}`));

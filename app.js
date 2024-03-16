
const express = require('express');
const app = express();
const fs = require('fs').promises; // Using fs.promises for asynchronous file operations

app.use(express.static('public'));


const port = 3000;

// Set EJS as the view engine
app.set('view engine', 'ejs');
// Define a route to render an EJS template
app.get('/', (req, res) => {
    res.render('commitee');
});


app.get('/:info', async (req, res) => {
    try {
        // Read the JSON file asynchronously
        const data = await fs.readFile('public/council_committee_JSON.json', 'utf8');
        const jsonData = JSON.parse(data);

        // Filter the data based on the parameter
        const filteredData = jsonData.filter(item => item.Category === req.params.info);

        // Send the filtered data as response
        res.render('commitee_members', { filteredData });
    } catch (err) {
        console.error('Error reading file:', err);
        res.status(500).send('Error reading file');
    }
});


app.get('/:info/:commitee', async (req, res) => {
  res.send('hi')
});

// Start the server
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});

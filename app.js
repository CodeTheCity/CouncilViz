const express = require('express');
const app = express();

app.use(express.static('public'));


const port = 3000;

// Set EJS as the view engine
app.set('view engine', 'ejs');
// Define a route to render an EJS template
app.get('/', (req, res) => {
    res.render('commitee');
});


app.get('/commitee/:info', (req, res) => {

    const data = {}

    res.render('commitee_members', data)
})
// Start the server
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});

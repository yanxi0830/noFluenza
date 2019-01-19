//random change
'use strict';

const express = require('express');
const port = process.env.PORT || 8080;
const bodyParser = require('body-parser');

// Import mongoose connection
const { mongoose } = require('./db/mongoose');

const { Info } = require('./models/model.js');

// load express
const app = express();
app.use(express.static(__dirname));
app.use(bodyParser.json());

// get app html page
app.get('/', (req, res) => {
    res.status(200).sendFile(__dirname + '/app.html');
});

app.listen(port, () => {
	console.log(`Listening on port ${port}...`);
});
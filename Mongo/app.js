const express = require('express');
require('dotenv/config');
const app = express();
const mongoose = require('mongoose');

//import routes
const postsRoute = require('./routes/posts');

app.use('/posts', postsRoute);

//Routes
app.get('/', (req, res) => {
    res.send('We are on home');
});
//Connect to DB
mongoose.connect(process.env.DB_CONNECTION
    , { useNewUrlParser: true }
    ,() => console.log('conected to DB'));
//start listening

app.listen(3000);

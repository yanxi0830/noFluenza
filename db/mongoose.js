const mongoose = require('mongoose');

const local = 'mongodb://localhost:27017/whyLike_test';
const remote = 'mongodb://sdy1130:look1130@ds145329.mlab.com:45329/whylike';

mongoose.connect(remote, { useNewUrlParser: true});

module.exports = { mongoose };
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const InfoSchema = new Schema({
	_id: Schema.Types.ObjectId
});

const Info = mongoose.model('Info', InfoSchema);

module.exports = { Info };

const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const Schema = mongoose.Schema;

const UserSchema = new Schema({
	_id: Schema.Types.ObjectId, 
	name: String,
	userID: String,
	image: String,
	location: String,
	phoneNum: String,
	email: {
		type: String,
		required: true,
		trim: true,
		unique: true
	},
	password: {
		type: String,
		required: true,
		minLength: 6
	},
	aboutMe: String,
	role: String,
	restaurantReviews: [{ type: Schema.Types.ObjectId, ref: 'RestaurantReview' }],
	dishReviews: [{ type: Schema.Types.ObjectId, ref: 'DishReview'}],
	restaurantsFollowing: [{ type: Schema.Types.ObjectId, ref: 'Restaurant'}],
	following: [{ type: Schema.Types.ObjectId, ref: 'User'}],
	follwers: [{ type: Schema.Types.ObjectId, ref: 'User'}]
});

const Information = mongoose.model('User', UserSchema);

module.exports = { User };

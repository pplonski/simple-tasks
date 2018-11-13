import { GET_ERRORS } from '../actions/types';

const initialState = {};

export default function(state = initialState, action) {
	switch(action.type) {
		case GET_ERRORS:
			//console.log(typeof action.payload)
			if(typeof action.payload === 'object') {
				return action.payload;
			} else if (typeof action.payload === 'string') {
				let errors = {}
				errors.non_field_errors = action.payload
				console.log(errors);
				return errors
			}
			return state;
		default:
			return state;
	}
}
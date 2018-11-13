import axios from 'axios';
import setAuthToken from '../utils/setAuthToken';

import { GET_ERRORS, SET_CURRENT_USER, UNSET_CURRENT_USER } from './types';

// Sign Up User
export const signUpUser = (userData, history) => dispatch => {
	axios.post('/api/auth/register/', userData)
			.then(res => history.push('/sign-in/'))
			.catch(err => 
				dispatch({
					type: GET_ERRORS,
					payload: err.response.data
				})
			);
};

// Sign In User
export const signInUser = (userData) => dispatch => {
	axios.post('/api/auth/login/', userData)
			.then(res => {
				// Save to local storage
				const { key } = res.data;
				// Set key to localStorage
				localStorage.setItem('authTokenKey', key);
				// Set token to Auth header
				setAuthToken(key);
				// Set current user
				dispatch(setCurrentUser());
			})
			.catch(err => 
				dispatch({
					type: GET_ERRORS,
					payload: err.response.data
				})
			);
};

export const setCurrentUser = () => dispatch => {
	axios.get('/api/auth/user/')
		.then(res => 
			dispatch({
				type: SET_CURRENT_USER,
				payload: res.data
			})
		)
		.catch(err => 
			dispatch({
				type: GET_ERRORS,
				payload: err.response.data
			})
		);
};

export const unsetCurrentUser = () => {
	return {
		type: UNSET_CURRENT_USER,
		payload: {}
	}
}

// Log user out
export const signOutUser = () => dispatch => {
	// Remove token from localStorage
	localStorage.removeItem('authTokenKey');
	// Remove auth header for future requests
	setAuthToken(false);
	// Set current user to {} which will set isAuthenticated to false
	dispatch(unsetCurrentUser());
}
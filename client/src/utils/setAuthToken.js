import axios from 'axios';

const setAuthToken = token => {
	if(token) {
		// Apply for every request
		axios.defaults.headers.common['Authorization'] = ("Token " + token);
	} else {
		// Delete auth header
		delete axios.defaults.headers.common['Authorization'];
	}
}

export default setAuthToken;
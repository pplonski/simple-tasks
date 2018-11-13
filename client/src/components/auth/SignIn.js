import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { signInUser } from '../../actions/authActions';
import TextFieldGroup from '../common/TextFieldGroup';

class SignIn extends Component {
	constructor() {
		super();
		this.state = {
			email: '',
			password: '',
			errors: {}
		};

		this.onChange = this.onChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	componentDidMount() {
		// if(this.props.auth.isAuthenticated) {
		// 	this.props.history.push('/tasks');
		// }
		console.log(localStorage.getItem('sessionid'))
	}

	componentWillReceiveProps(nextProps) {
		if(nextProps.errors) {
			this.setState({ errors: nextProps.errors });
		}
	}

	onChange(e) {
		this.setState({ [e.target.name]: e.target.value });
	}

	onSubmit(e) {
		e.preventDefault();

		const userData = {
			username: this.state.username,
			email: this.state.email,
			password: this.state.password
		}

		this.props.signInUser(userData);
	
	}

	render() {
		const { errors } = this.state;

		return(
			<div className="sing-in">
		    <div className="container">
		      <div className="row">
		        <div className="col-md-8 m-auto">
		          <h1 className="display-4 text-center">Sign In</h1>
		          <p className="lead text-center">Sign in to your Simple Tasks account</p>

		          <form noValidate onSubmit={this.onSubmit}>
		            <TextFieldGroup
									placeholder="Email"
									name="email"
									type="email"
									value={this.state.email}
									onChange={this.onChange}
									error={errors.email}
								/>

		            <TextFieldGroup
									placeholder="Password"
									name="password"
									type="password"
									value={this.state.password}
									onChange={this.onChange}
									error={errors.password}
								/>

		            <input type="submit" className="btn btn-info btn-block mt-4" value="Submit" />
		          </form>

		        </div>
		      </div>
		    </div>
		  </div>
		)
	}
}

const mapStateToProps = (state) => ({
	auth: state.auth,
	errors: state.errors,
});

SignIn.propTypes = {
	signInUser: PropTypes.func.isRequired,
	auth: PropTypes.object.isRequired
};

export default connect(mapStateToProps, { signInUser })(SignIn);
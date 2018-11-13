import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { signUpUser } from '../../actions/authActions';
import TextFieldGroup from '../common/TextFieldGroup';

class SignUp extends Component {
	constructor() {
		super();
		this.state = {
			username: '',
			email: '',
			password1: '',
			password2: '',
			errors: {}
		};

		this.onChange = this.onChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	// componentDidMount() {
	// 	if(this.props.auth.isAuthenticated) {
	// 		this.props.history.push('/tasks');
	// 	}
	// }

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

		const newUser = {
			username: this.state.username,
			email: this.state.email,
			password1: this.state.password1,
			password2: this.state.password2
		}

		this.props.signUpUser(newUser, this.props.history);
	
	}

	render() {
		const { errors } = this.state;

		return(
			<div className="sing-up">
		    <div className="container">
		      <div className="row">
		        <div className="col-md-8 m-auto">
		          <h1 className="display-4 text-center">Sign Up</h1>
		          <p className="lead text-center">Create your Simple Tasks account</p>

		          <form noValidate onSubmit={this.onSubmit}>
		          	<TextFieldGroup
									placeholder="Username"
									name="username"
									value={this.state.username}
									onChange={this.onChange}
									error={errors.username}
								/>

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
									name="password1"
									type="password"
									value={this.state.password1}
									onChange={this.onChange}
									error={errors.password1}
								/>

		            <TextFieldGroup
									placeholder="Confirm Password"
									name="password2"
									type="password"
									value={this.state.password2}
									onChange={this.onChange}
									error={errors.password2}
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

SignUp.propTypes = {
	signUpUser: PropTypes.func.isRequired,
	auth: PropTypes.object.isRequired
};

export default connect(mapStateToProps, { signUpUser })(withRouter(SignUp));
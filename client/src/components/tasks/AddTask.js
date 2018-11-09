import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import isEmpty from '../../validation/isEmpty';

import TextFieldGroup from '../common/TextFieldGroup';

import { addTask } from '../../actions/tasksActions';

class AddTask extends Component {
	constructor(props) {
		super(props);
		this.state = {
			params: {},
			arg1: '',
			arg2: '',
			errors: {
				params: {}
			}
		}
		this.onChange = this.onChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	componentWillReceiveProps(nextProps) {
		if(!isEmpty(nextProps.errors)) {
			//console.log('nextProps errors');
			//console.log(nextProps.errors);
			//console.log('-----------------');
			this.setState({ errors: nextProps.errors })
		}
	}

	onSubmit(e) {
		e.preventDefault();

		const arg1 = (this.state.arg1) ? {"arg1": parseInt(this.state.arg1)} : {};
		const arg2 = (this.state.arg2) ? {"arg2": parseInt(this.state.arg2)} : {};
		let params;
		params = Object.assign(arg1, arg2);

		const taskData = {
			params: params
		}
		this.props.addTask(taskData, this.props.history)
	}

	onChange(e) {
		this.setState({ [e.target.name]: e.target.value })
	}

	render() {
		const { errors } = this.state;
		
		return(
			<div className="container">
				<h1>Add task</h1>
				<hr/>
				{('global' in errors) && <div className="badge badge-danger mb-3">{errors.global}</div>}

				<form onSubmit={this.onSubmit}>
					<TextFieldGroup
						placeholder="arg1"
						name="arg1"
						value={this.state.arg1}
						onChange={this.onChange}
						error={ ('params' in errors) ? errors.params.arg1 : [] }
					/>
					<TextFieldGroup
						placeholder="arg2"
						name="arg2"
						value={this.state.arg2}
						onChange={this.onChange}
						error={ ('params' in errors) ? errors.params.arg2 : [] }
					/>
					<input type="submit" value="Submit" className="btn btn-info mt-2" />
					<Link to="/tasks" className="btn btn-default mt-2">Back</Link>
				</form>
			</div>
		)
	}
}

AddTask.propTypes = {
	addTask: PropTypes.func.isRequired,
	tasks: PropTypes.object.isRequired,
	errors: PropTypes.object.isRequired
}

const mapStateToProps = state => ({
	tasks: state.tasks,
	errors: state.errors
});

export default connect(mapStateToProps, { addTask })(withRouter(AddTask));
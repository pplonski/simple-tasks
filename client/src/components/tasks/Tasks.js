import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Progress } from 'reactstrap';
import classnames from 'classnames';

import { getTasks } from '../../actions/tasksActions';
import { getCompletedTask } from '../../actions/tasksActions';
import { deleteTask } from '../../actions/tasksActions';

class Tasks extends Component {
	componentDidMount() {
		this.props.getTasks()
	}
	componentDidUpdate(prevProps) {
		if(this.props.tasks.completedTask!==prevProps.tasks.completedTask) {
			this.props.getCompletedTask(this.props.tasks.completedTask);
		}
	}
	onDeleteClick(id) {
		this.props.deleteTask(id);
	}

	render() {
		const { tasks, loading } = this.props.tasks;
		let tasksItems;
		//console.log(this.props)

		if(tasks === null || loading) {
			tasksItems = <div>Loading...</div>
		} else {
			if(tasks.length > 0) {
				tasksItems = tasks.map(task => {
					let taskResult;

					if("data" in task.result) {
						taskResult = task.result.data
					} else if("exception" in task.result) {
						taskResult = task.result.exception
					} else {
						taskResult = 'Waiting...'
					}

					let taskProgress;
					if(task.state==='SUCCESS') {
						taskProgress = (<Progress color="success" value="100" className="mb-1">100%</Progress>)
					} else {
						taskProgress = (<Progress value={task.progress} className="mb-1">{task.progress}%</Progress>)
					}

					return(
						<div className="border-bottom" key={task.id}>
							<div className="row mt-3 mb-3">
								<div className="col-md-8">
									<b>Id:</b> {task.id} <br/>
									<b>Task_id:</b> {task.task_id} <br/>
									<b>State:</b> {' '}
										<span
											className={classnames( 'badge',
												{'badge-success': ( task.state === 'SUCCESS' )},
												{'badge-info': ( task.state === 'CREATED' )},
												{'badge-info': ( task.state === 'PROGRESS' )},
												{'badge-danger': ( task.state === 'FAILURE' )}
											)}
										>
											{task.state}
										</span> {' '} <br/>
									<b>Result:</b> {taskResult} {' '} <br/>
									<b>Params:</b> <span className="badge badge-light">arg1:</span> {task.params.arg1} <span className="badge badge-light">arg2:</span> {task.params.arg2}
								</div>
								<div className="col-md-3 mt-2">
									{taskProgress}
								</div>
								<div className="col-md-1">
									<button
										className="btn btn-default btn-sm"
										onClick={this.onDeleteClick.bind(this, task.id)}
									>
										Delete
									</button>
								</div>
							</div>
						</div>
					)
				});
			} else {
				tasksItems = <div>No tasks found...</div>
			}
		}


		return(
			<div className="container">
				<div className="row">
					<div className="col-md-10">
						<h1>Tasks</h1>
					</div>
					<div className="col-md-2">
						<Link to="/tasks/add/" className="btn btn-primary mt-2 btn-block">Add task</Link>
					</div>
				</div>
				<hr/>
				{tasksItems}
			</div>
		)
	}
}

Tasks.propTypes = {
	getTasks: PropTypes.func.isRequired,
	getCompletedTask: PropTypes.func.isRequired,
	deleteTask: PropTypes.func.isRequired,
	tasks: PropTypes.object.isRequired
}

const mapStateToProps = state => ({
	tasks: state.tasks
});

export default connect(mapStateToProps, { getTasks, getCompletedTask, deleteTask })(withRouter(Tasks));

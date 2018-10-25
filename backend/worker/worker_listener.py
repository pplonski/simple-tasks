from simple_worker import WORKERS
from task_updater import TaskUpdater


def my_monitor(app):
    state = app.events.State()

    def announce_received_tasks(event):
        state.event(event)

        if 'uuid' not in event:
            return

        task = state.tasks.get(event['uuid'])
        
        # update DB
        new_result = {'exception': event['exception']} if 'exception' in event else None
        db_id = TaskUpdater.update_db(task_id = event['uuid'], new_state=event['state'], new_result=new_result)
        # send to channel
        data = {'state': event['state'], 'db_id': db_id}
        msg = {"type": "task_update_message", "data": data}
        TaskUpdater.update_ws(msg)

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-failed': announce_received_tasks,
                'task-rejected': announce_received_tasks,
                'task-revoked': announce_received_tasks,
                'task-retried': announce_received_tasks
        })
        #
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    my_monitor(WORKERS)

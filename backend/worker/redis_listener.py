'''This script observes redis chanels and send task's progress update to websocket channel'''''
import json
import redis
import time
import os
import sys
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BACKEND_DIR)
from config import REDIS_URL, REDIS_PORT

from task_updater import TaskUpdater

CELERY_CHANNELS = 'celery-task-meta-*'

def extract_msg(item):
    ''' Converting redis message into message send to web socket channel '''
    if item.get('type') is None or item.get('type') != 'pmessage':
        return None
    print(item)
    try:
        item_data = json.loads(item['data'].decode('utf8').replace("'", '"'))
    except json.decoder.JSONDecodeError as e:
        # This can happen when task failed
        return None
    if item_data['status'] not in ['PROGRESS']: #, 'SUCCESS']:
        return None
    if item_data.get('status') is None:
        return None

    progress = item_data['result']['progress'] if item_data['status'] == 'PROGRESS' else 100

    data = {'state': item_data['status'],
            'progress': progress,
            'db_id': item_data['result']['db_id']}

    print('{0} {1} {2}'.format(data['db_id'],
                                item_data['status'],
                                progress))
    msg = {"type": "task_update_message", "data": data}

    return msg

def get_redis_connection():
    redis_instance = None

    try:
        redis_instance = redis.StrictRedis(host=REDIS_URL, port=REDIS_PORT, db=0)
        redis_instance.ping()
        return redis_instance
    except Exception as e:
        time.sleep(5)
        redis_instance = redis.StrictRedis(host=REDIS_URL, port=REDIS_PORT, db=0)
        redis_instance.ping()

    return redis_instance

def main():
    ''' Running redis listener and sending updates to websocket channel '''
    print('start')

    redis_instance = get_redis_connection()
    if redis_instance is None:
        return
    pubsub = redis_instance.pubsub()
    pubsub.psubscribe(CELERY_CHANNELS)

    for item in pubsub.listen():
        msg = extract_msg(item)
        if msg is None:
            continue
        # send to channel
        TaskUpdater.update_ws(msg)


if __name__ == '__main__':
    main()

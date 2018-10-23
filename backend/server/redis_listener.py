'''This script observes redis chanels and send task's progress update to websocket channel'''''
import json
import redis

from server.asgi import *
from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

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
    if item_data['status'] not in ['PROGRESS', 'SUCCESS']:
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

def main():
    ''' Running redis listener and sending updates to websocket channel '''
    channel_layer = get_channel_layer()
    redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
    pubsub = redis_instance.pubsub()
    pubsub.psubscribe(CELERY_CHANNELS)

    for item in pubsub.listen():
        msg = extract_msg(item)
        if msg is None:
            continue
        # send to channel
        async_to_sync(channel_layer.group_send)("tasks", msg)


if __name__ == '__main__':
    main()

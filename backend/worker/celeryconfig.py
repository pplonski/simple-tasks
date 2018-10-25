
from config import BROKER_URL, REDIS_URL, REDIS_PORT

broker_url = BROKER_URL
result_backend = 'redis://{0}:{1}'.format(REDIS_URL, REDIS_PORT)
task_serializer = 'json'
task_acks_late = True
worker_concurrency = 2

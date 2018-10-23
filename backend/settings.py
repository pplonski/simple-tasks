import os

BROKER_URL = os.environ.get('BROKER_URL', 'pyamqp://guest@localhost//')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost') # 'redis://redis:6379/0')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379') # 'redis://redis:6379/0')


DATABASE_URL = os.environ.get('DATABASE_URL', '127.0.0.1')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'simple_tasks')
DATABASE_USER = os.environ.get('DATABASE_USER', 'postgres')
DATABASE_PASS = os.environ.get('DATABASE_PASS', '1234')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5433')

# sudo docker run --rm -P -p 127.0.0.1:5433:5432 -e POSTGRES_PASSWORD="1234" --name pg postgres:9.6-alpine

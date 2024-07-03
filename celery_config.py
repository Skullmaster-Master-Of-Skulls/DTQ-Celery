from celery import Celery

app = Celery('tasks', broker='redis://:redisisgoated@127.0.0.1:6379/0')

app.conf.update(
    result_backend='redis://:redisisgoated@127.0.0.1:6379/0',
    include=['tasks']
)

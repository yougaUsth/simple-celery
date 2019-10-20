# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from kombu import Exchange, Queue

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Asia/Shanghai'

BROKER_URL = "amqp://guest:guest@127.0.0.1:5672"

CELERY_ACKS_LATE = False

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 180000}
CELERYD_MAX_TASKS_PER_CHILD = 200
CELERY_IGNORE_RESULT = True

CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_SEND_TASK_ERROR_EMAILS = True

CELERY_ACCEPT_CONTENT = ['json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

default_exchange = Exchange('default', type='direct')

CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('mq', default_exchange, routing_key='mq'),

)

CELERY_ROUTES = (
    {
        'celery_task.test_add.add': {
            'queue': 'default',
            'routing_key': 'default'
        }
    }
)

CELERY_IMPORTS = (
    'celery_task.test_add',
)


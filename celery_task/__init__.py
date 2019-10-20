# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import Celery, platforms


app = Celery("task")
app.config_from_object('celery_task.celery_config')

platforms.C_FORCE_ROOT = True

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from celery_task import app

PCAP_FILE_PATH = "/Users/data"


@app.task(name='celery_task.test_add.add')
def add(file_name):

    if not os.path.exists(PCAP_FILE_PATH+file_name):
        return
    r = open(PCAP_FILE_PATH+file_name, "r").read()
    print r
    os.remove(os.path.join(PCAP_FILE_PATH, file_name))
    return file_name


if __name__ == '__main__':
    pass

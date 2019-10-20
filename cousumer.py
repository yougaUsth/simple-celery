# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import os

from celery_task import test_add

PCAP_FILE_PATH = "/User/data"


if __name__ == '__main__':
    _c = 1
    while True:
        print _c
        _c += 1
        files = os.listdir("")
        if files:
            files = set(files)
            print len(files), "Task to do"
            for file_name in files:
                test_add.add.delay(file_name)
            time.sleep(60 * 10)
        else:
            time.sleep(10)
            print "No Task to run Pending!"

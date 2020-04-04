# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

import datetime
import time

time_now = datetime.datetime.now()
time_now_formatted = time_now.strftime(format='%H:%M:%S')

time_epoch = datetime.datetime.strptime('1970-01-01', '%Y-%m-%d')

time_delta = (time_now - time_epoch).days

print('Time now in your system in HH:MM:SS {}'.format(time_now_formatted))
print('No. of days passed since the epoch {}'.format(time_delta))
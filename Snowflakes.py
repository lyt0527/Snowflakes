#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import threading
import datetime


class Snow(object):
 
    def __init__(self, idx=None):
        init_date = time.strptime('2020-04-01 00:00:00', "%Y-%m-%d %H:%M:%S")
        self.start = int(time.mktime(init_date) * 1000)
        self.last = int(time.time() * 1000)
        self.count_id = 0
        self.idx = idx if idx else 0
 
    def get(self):
        now = int(time.time() * 1000)
        temp = now - self.start
        if len(str(temp)) < 12:
            length = len(str(temp))
            s = '0' * (12 - length)
            temp = s + str(temp)
        if now == self.last:
            self.count_id += 1
        else:
            self.count_id = 0
            self.last = now
        if len(str(self.idx)) < 2:
            length = len(str(self.idx))
            s = '0' * (2 - length)
            self.idx = s + str(self.idx)
        if self.count_id == 99999:
            time.sleep(1)
        count_id_data = str(self.count_id)
        if len(count_id_data) < 5:
            length = len(count_id_data)
            s = '0' * (5 - length)
            count_id_data = s + count_id_data
        return ''.join([str(temp), str(self.idx), count_id_data])
    
snow = Snow('00')
l = []
for i in range(536):
    l.append(snow.get())


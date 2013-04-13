#!/usr/bin/env python

import json
import urllib
import time
import math

url = "http://hhtt.1209k.com/user-details-json.php?user=1LFCYbHzM3AhfE6dfjypenzbju8qVZyese"

def average(l):
    return reduce(lambda x, y: x + y, l) / len(l)

response = urllib.urlopen(url)
shares = json.loads(response.read())["shares"]
times = []
for share in shares:
    if type(shares[share]) is dict:
        times.append(shares[share]["time"].split(" ")[1])
times.sort()
intervals = []
for idx, tm in enumerate(times):
    if idx >= 1:
        t1 = time.mktime(time.strptime(tm, "%H:%M:%S"))
        t2 = time.mktime(time.strptime(times[idx-1], "%H:%M:%S"))
        intervals.append((t1 - t2) / 60)

mean_share_interval = average(intervals)
print "mean share interval: {0} minutes".format(mean_share_interval)
variance = map(lambda x: (x - mean_share_interval)**2, intervals)
print "standard deviation: {0}".format(math.sqrt(average(variance)))
print "min/max intervals: {0}/{1}".format(min(intervals), max(intervals))

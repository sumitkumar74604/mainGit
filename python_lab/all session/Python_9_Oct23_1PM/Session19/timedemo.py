'''
Time Module: This module is used to get time related implementation in python.
In Python, the time() function returns the number of seconds passed since epoch (the point where time begins). 

Epoch Converter - Unix Timestamp Converter
What is epoch time? The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds
'''

import time

epoch=time.time()
print("Epoch Time in seconds:",epoch)
print("================================================")

localtime_tuple = time.localtime(epoch)
print("Local Time in tuple:",localtime_tuple)
print("================================================")

asctime = time.asctime(localtime_tuple)
print("Current Day and Time is:",asctime)
print("================================================")

gmtime_tuple = time.gmtime(epoch)
print("GM Time Tuple is:",gmtime_tuple)
print("================================================")
usable_gmtime = time.asctime(gmtime_tuple)
print("GM Time is:",usable_gmtime)

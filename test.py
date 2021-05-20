import time
import datetime
d = datetime.date(2021,5,19)

unixtime = time.mktime(d.timetuple())

print(d, '=', int(unixtime))

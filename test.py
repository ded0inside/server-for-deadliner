from datetime import datetime
import time
date_in_datetime = datetime(2020, 3, 2)
unix_time = time.mktime(date_in_datetime.timetuple())
print(int(unix_time))
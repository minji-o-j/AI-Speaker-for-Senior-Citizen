from datetime import datetime 

now = datetime.now()
month = now.month
date = str(now.month).zfill(2) + str(now.day).zfill(2)
print(int(date))
date = int(date)
time = str(now.hour).zfill(2) + str(now.minute).zfill(2)
print(int(time))
time = int(time)
print('%02d%02d' % (now.month, now.day))
print('%02d%02d' % (now.hour, now.minute))
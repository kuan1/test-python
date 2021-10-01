from datetime import datetime, time

# Getting datetime infomation
now = datetime.now()
print(now)

print(now.weekday())
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)
print(now.timestamp())

# Formatting Date Output Using strftime
new_time = datetime(2020, 1, 1)
print(new_time.timestamp())
print("time: ", now.strftime('%H:%M:%S'))
print("Date Time: ", now.strftime('%Y-%m-%d %H:%M:%S'))

print(now.today())

number = int(input())
hours = int(number // (60 * 60) % 24)
minutes = int((number // 60) % 60)
second = int(number % 60)
r_hour = str(hours)
r_minute = str(minutes // 10) + str(minutes % 10)
r_second = str(second // 10) + str(second % 10)
print(r_hour + ':' + r_minute + ':' + r_second)

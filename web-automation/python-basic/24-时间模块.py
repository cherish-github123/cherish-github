import calendar
import time
import datetime
# 获取当前时间戳
print(time.time())

# 获取当前时间
print(time.localtime())
# 结果：time.struct_time(tm_year=2024, tm_mon=5, tm_mday=11, tm_hour=17, tm_min=0, tm_sec=2, tm_wday=5, tm_yday=132, tm_isdst=0)

# 获取格式化的时间
print(time.asctime())  # Sat May 11 17:00:02 2024

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 结果:2024-05-11 17:02:00

# 获取某年某月的日历,2024年5月的日历
print(calendar.month(2024, 5))


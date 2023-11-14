# 10699 -> 15일 6시 이후 다시 제출 (백준 제출 시간대 환경이 안맞음)
import datetime as dt
now = dt.datetime.today()
print(now.year,now.month,now.day, sep='-')

# 2번 방법
print(dt.date.today())
# 3번 방법
print(str(dt.datetime.today())[:10])

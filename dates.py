from datetime import datetime, timedelta

now = datetime.now()
two_day = timedelta(weeks=2)
print(now - two_day)
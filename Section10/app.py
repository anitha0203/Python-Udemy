from datetime import datetime, timezone, timedelta

print(datetime.now())

print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M'))             # strftime  -      string format time

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')        #   strptime  -     string parse time

print(user_date)


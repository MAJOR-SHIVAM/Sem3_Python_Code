import datetime
from dateutil.relativedelta import relativedelta
# print(dir(datetime))
t = datetime.time( 2)
print(t)

t = datetime.time(minute=2)
print(t)

print (f'hour : {t.hour}')
print (f'minute: {t.minute}')
print (f'second: {t.second}')
print (f'microsecond: {t.microsecond}')
print (f'tzinfo: {t.tzinfo}')


print ('Earliest :', datetime.time.min)
print ('Latest :', datetime.time.max)
print ('Resolution:', datetime.time.resolution)




t = datetime.time(microsecond=5, minute=39)
print(t)



print("--------------------------------------------------")

today = datetime.date.today()
print (f'today: \n\t {today}')
print (f'ctime: \n\t {today.ctime()}')
print (f'tuple: \n\t {today.timetuple()}')
print (f'ordinal: \n\t {today.toordinal()}')
print (f'Year: \n\t {today.year}')
print (f'Mon: \n\t {today.month}')
print (f'Day: \n\t {today.day}')



print("---------------------------------------------")

o = 739058
print (f'o = {o} and fromordinal(o) = {datetime.date.fromordinal(o).isoformat()}')

# the number of days since 1st Jan 1 AD
# that is the epoch reference date
# the ordianl for 1st Jan 1 AD is 1
# the ordinal for 2nd Jan 1 AD is 2
# the ordinal for 3rd Jan 1 AD is 3
# 
# the ordinal for 1st Jan 2020 is 737061
# the ordinal for 2nd Jan 2020 is 737062
# the ordinal for 3rd Jan 2020 is 737063
# 
# the ordinal for 1st Jan 2021 is 738396
# the ordinal for 2nd Jan 2021 is 738397
# the ordinal for 3rd Jan 2021 is 738398
# 
# the ordinal for 1st Jan 2022 is 739058
# the ordinal for 2nd Jan 2022 is 739059
# the ordinal for 3rd Jan 2022 is 739060
# 
# and so on.




# What is AD
# AD is Anno Domini
# it is a year numbering system based on the traditionally recognized date of the birth of Jesus Christ
# it is based on a 6th century estimate of the birth of Jesus Christ
# it is used to number the years in the Gregorian calendar
# it is used to number the years in the Julian calendar
# it is used to number the years in the Ethiopian calendar

print("---------------------------")
print (f'Earliest: {datetime.date.min}')
print (f'Latest: {datetime.date.max}')
print (f'Resolution: {datetime.date.resolution}')

print("----------------------------")
print (f"microseconds: {datetime.timedelta(microseconds=1)}")
print (f"milliseconds: {datetime.timedelta(milliseconds=1)}")
print (f"seconds: {datetime.timedelta(seconds=1)}")
print (f"minutes: {datetime.timedelta(minutes=1)}")
print (f"hours: {datetime.timedelta(hours=1)}")
print (f"days: {datetime.timedelta(days=1)}")
print (f"weeks: {datetime.timedelta(weeks=1)}")



#take todays date and time what will be the date after 1 day 8 hours using time delta
print("--------------------------------------------------------")

today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1, hours=8)
print("Today:", today)
print("Tomorrow after 8 hours: ",tomorrow)



print("--------------------------------------------------")

d = datetime.datetime.today()
new_date = d + datetime.timedelta(weeks=5)
print("After 5 weeks: ", new_date)


# aaj se 2 saal 3 mahine and 4 months what was the datetime



print("--------------------------------------------------")


d = datetime.datetime.today()
new_date = d - datetime.timedelta(weeks = 120)
print("2 years, 3 months and 4 weeks ago: ", new_date)



print("-------------------------------------------------------")
print(f'Now: {datetime.datetime.now()}')
print(f'Today: {datetime.datetime.today()}')
print(f'UTC Now: {datetime.datetime.utcnow()}')
d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second']:
    print(f"{attr}: {getattr(d, attr)}")



print("-----------------------------------------------------")

t = datetime.time(1, 2, 3)
print (f't : {t}')
d = datetime.date.today()
print (f'd : {d}')
dt = datetime.datetime.combine(d, t)
print (f'dt: {dt}')

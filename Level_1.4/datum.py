import calendar

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date = input().split(" ")

day = int(date[0])
month = int(date[1])
year = 2009

print(weekdays[calendar.weekday(year,month,day)])






# months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 01/01/2009 was a Thursday
# day = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

# total_days = 0
# for i in range(month):
#    total_days += months[i]
# total_days += day

# print(day[total_days % 7 - 1])
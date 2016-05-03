#Python 3.6 Documentation via https://docs.python.org/3.6/library/calendar.html?highlight=calendar#module-calendar
import calendar as cal

#Determine if a year is leap
cal.isleap(2018)

#Determine the number of leap years with a range of years, exclusive of last year
cal.leapdays(2000,2051)

#Determine the day of the week for a particular date. Monday is 0; Tuesday is 1 etc
cal.weekday(2016,3,21)

Y=int(input("Enter the Year:"))
M=int(input("Enter the Month:"))
D=int(input("Enter the Day:"))
Today=cal.weekday(Y,M,D)
Days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(0,7,1):
    if i == Today:
        print(Days[i])

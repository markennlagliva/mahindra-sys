from datetime import datetime

currentDate = datetime.now()
print(2 > 1)
print(1 > 1 or 1 == 1)

import datetime
print('Current Month:',datetime.datetime.now().month)
# Get the current year
current_year = datetime.datetime.now().year

# Print the current year
print('This is current year:',current_year)

date = currentDate.date() # For Date
time = currentDate.time()


print(time)
print(date)
status = time.strftime('%p')
print(status)
if status == 'AM':
    time_in = time.strftime('%H:%M:%S')
    formatted_time_12h = time.strftime('%I:%M %p')
    print('this is time_in:',time_in)
    print('12hour format:', formatted_time_12h)
    obj = str(time_in).split(':')[0]
    print('Morning')
    if obj[0] == '0':
        pass
    
    
else:
    time_out = time.strftime('%H:%M:%S')
    formatted_time_12h = time.strftime('%I:%M %p')
    print(formatted_time_12h)
    print('Afternoon')


# date = current_datetime.date() #this
# time = current_datetime.time()

# time_in = time.strftime('%H:%M:%S')
# formatted_time_12h = time.strftime('%I:%M:%p') #This
# print(formatted_time_12h)

# status = time.strftime('%p')
# print(status)

# time_in_time = [x for x in time_in.split(':')]
# print(time_in)
# print('This is time in: ', time_in_time)


# time_out_str = "16:45:00"
# time_out_time = [x for x in time_out_str.split(':')]
# print('This is time out: ', time_out_time)

# print(time_in_time[0])
# print(time_out_time[0])

# print('total hours:',int(time_out_time[0]) - int(time_in_time[0]))


# print((17 - 8) - 1)










import csv
import numpy

from datetime import datetime
filename = 'weather_data.csv'
months = [' ', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
# 1 What 3 year period had the highest change in actual mean Temperature?
threeYearTempCh = {}
def year_average(x):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        years = []
        actual_mean_temp = []


        for row in reader:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            if current_date.year ==x:
                year = int(row[1])
                actual_mean_temp.append(year)
                average_temp = numpy.mean(actual_mean_temp)

                return average_temp

for x in range(1992,2015):
    change_temp = abs((year_average(x) - year_average(x+3)))
    print('\tPeriod between {0} - {1} has actual mean Temperature change of  \t{2} F'.format(x,(x + 3), change_temp))

print("2002 to 2005 has the highest period of change in actual mean temperature")


# 2 What month has the highest actual Max Temperature on Average across 25 years?

tempVal = {}

def weather(x):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        highs = []

        for row in reader:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            if current_date.month == x:
                high = int(row[3])
                highs.append(high)
                average_month = int(sum(highs)) / len(highs)

        tempVal.update({months[x]: average_month})
        print('{0} {1}'.format(months[x], average_month))


for x in range(1, 13):
    weather(x)

highest_temp = max(tempVal.values())
highest_temp_key = [k for k, v in tempVal.items() if v == highest_temp]

print ('In 25 years ' + ",".join(highest_temp_key) + ' has the highest temperate')


# 3 What month on average had the highest difference between the actual low and actual high temperature on a given day across all 25 years?


tempDiffVal = {}

def weather(x):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        highs = []
        mins = []
        difference =[]


        for row in reader:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            if current_date.month ==x:
                high = int(row[3])
                highs.append(high)
                highTemp_month = int(sum(highs)) / len(highs)
                min = int(row[2])
                mins.append(min)
                min_month = int(sum(mins)) / len(mins)
                difference = float (highTemp_month - min_month)

        tempDiffVal.update({months[x]: difference})
        print( '{0} {1}'.format(months[x], highTemp_month))
        print( '{0} {1}'.format(months[x], min_month))
        print('{0}'.format(difference))


for x in range(1,13):
    weather(x)

highestDiff_temp = max(tempDiffVal.values())
highestDiff_temp_key = [k for k, v in tempDiffVal.items() if v == highestDiff_temp]

print ('Across all 25 years ' + ",".join(highestDiff_temp_key) + ' had the highest difference between the actual low and actual high temperateure on a given day.')

# 4 What is the actual rainiest month on average

tempVal={}
def weather(x):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        highs = []

        for row in reader:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            if current_date.month ==x:
                high = float(row[10])
                highs.append(high)
                average_month = float(sum(highs)) / len(highs)
        tempVal.update({months[x]: average_month})
        print('{0} {1}'.format(months[x], average_month))


for x in range(1,13):
    weather(x)

highest_temp = max(tempVal.values())
highest_temp_key = [k for k, v in tempVal.items() if v == highest_temp]

print ('The rainiest month on average is ' + ",".join(highest_temp_key))

#5 In the last 25 years do we have more days that are above average precipitation or more days below?
import numpy as np

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    actual_precip = []
    average_precip = []




    for row in reader:
        actual_precip.append(row[10])
        average_precip.append(row[11])

    x = np.array(actual_precip)
    y = np.array(average_precip)
    above_average = np.count_nonzero(x > y)
    below_average = np.count_nonzero(x < y)
    equal = np.count_nonzero(x == y)

    print('\t{0} days above average precipitation.\t'.format(above_average))
    print('\t{0} days below average precipitation.\t'.format(below_average))

    if (below_average > above_average):
        print('In the last 25 years we have more days below average precipitation')
    else:
        print('In the last 25 years we have more days above average precipitation')
        

#6 a). Is Washington DC on average getting warmer, colder, or staying the same over the past 25 years?

dcTemps = []

def weather(x):
    with open (filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        actual_mean_temp = []

        for row in reader:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            if current_date.year ==(x):
                mean = int(row[1])
                actual_mean_temp.append(mean)
                average_temp = numpy.mean(actual_mean_temp)
        return average_temp


for x in range(1992,2017):
    year_average = weather(x)
    dcTemps.append(year_average)
    #print('\n The average temperature of Washington DC for Year ' + str(x) + ' is ' + str(year_average))

#print(dcTemps)

def moving_average(a, n=3):
    ret = numpy.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

if(numpy.all(numpy.diff(moving_average(numpy.array(dcTemps), len(dcTemps))>0))):
    print("Washington DC temperature on average is getting warmer over the past 25 years")
elif(not numpy.all(numpy.diff(moving_average(numpy.array(dcTemps), len(dcTemps))>0))):
    print("Washington DC temperature on average is getting colder over the past 25 years")
else:
    print("Washington DC temperature on average is staying the same over the past 25 years")


# b) What do you think the actual min and the actual max temperature will be on Thanksgiving 2017 (November 23rd)

filename = 'weather_data.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    min_temp, max_temp = [],[]
    for row in reader:
        date = datetime.strptime(row[0], "%m/%d/%Y")
        day = date.day
        month = date.month

        try:
            if month==11 and day==23:
                min_temp.append(int(row[2]))
                max_temp.append(int(row[3]))
        except ValueError:
            print(row, 'missing data')
        else:
            continue
min_average=sum(min_temp)/len(min_temp)
max_average=sum(max_temp)/len(max_temp)
print("Thanksgiving 2017 will have a min temperature of "+ str(min_average) +" and a max temperature of " + str(max_average))



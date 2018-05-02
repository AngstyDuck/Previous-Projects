def num_days_in_month(month_num, leap_year):
    if (leap_year):
        years = [31,29,31,30,31,30,31,31,30,31,30,31]
        return years[int(month_num-1)]
    elif not(leap_year):
        years = [31,28,31,30,31,30,31,31,30,31,30,31]
        return years[int(month_num-1)]
    else:
        print('leap year error')

def day_of_week_jan1(year):    #0-Sunday, 1-Monday
    def R(y,x):
        return y%x
    output = R(1+5*R(year -1,4)+4*R(year-1, 100) + 6*R(year-1,400),7)
    if ((year-1800)>=0) and (2099-year>=0):
        return output
    else:
        return "input year is out of range"

def leap_year(year): #leapyr-true, not-false
    if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
        return True
    else:
        return False

def day_of_week_jan1(year):    #0-Sunday, 1-Monday
    def R(y,x):
        return y%x
    output = R(1+5*R(year -1,4)+4*R(year-1, 100) + 6*R(year-1,400),7)
    if ((year-1800)>=0) and (2099-year>=0):
        return output
    else:
        return "input year is out of range"


def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    outputList = []
    monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    #adds month name into outputList
    outputList.append(monthList[month_num-1])
    
    #creates entireDayString, calendar with appropriate front space and spaces between numbers
    frontSpace = first_day_of_month * '   '
    daysList = []
    for i in range(1,num_days_in_month +1):
        iStr = str(i)
        if (len(iStr)==1):
            iStr = '  ' + iStr
        elif (len(iStr)==2):
            iStr = ' ' + iStr
        daysList.append(iStr)

    entireDayString = frontSpace + ''.join(daysList)

    #split entireDayString into appropriate lines and append to outputList
    rangeNum = 0
    """
    while (num_days_in_month*3 - rangeNum >= 0):
        sublist = entireDayString[rangeNum:rangeNum+21]
        outputList.append(sublist)
        rangeNum += 21
    
    
    sublistLeftover = entireDayString[rangeNum:]
    outputList.append(sublistLeftover)
    """
    
    while (len(entireDayString[rangeNum:])-21 >= 0):
        sublist = entireDayString[rangeNum:rangeNum+21]
        outputList.append(sublist)
        rangeNum += 21
    
    if (len(entireDayString) % 21 == 0):
        pass
    else:
        sublistLeftover = entireDayString[rangeNum:]
        outputList.append(sublistLeftover)

    return outputList


def construct_cal_year(year):
    year = int(year)
    leap_yearInput = leap_year(year)
    #first_day = day_of_week_jan1(year)
    first_day_of_monthInput = day_of_week_jan1(year)
    
    outputList = []
    outputList.append(year)
    for i in range(1,13):
        num_days_in_monthInput = num_days_in_month(i,leap_yearInput)
        outputList.append(construct_cal_month(i, first_day_of_monthInput, num_days_in_monthInput))
        #stringOfMonth = str.join('\n',construct_cal_month(i, first_day_of_month, num_days_in_month))
        
        #add code to combine the lists in construct_cal_month to one element of a list that represents one full month
        #print years
        
        
        move = num_days_in_monthInput % 7
        first_day_of_monthInput = first_day_of_monthInput + move
        if (first_day_of_monthInput >= 7):
            first_day_of_monthInput = first_day_of_monthInput - 7
    return outputList


def display_calendar(year):
    yearNestList = construct_cal_year(year)[1:]
    insertListElement = '  S  M  T  W  T  F  S'
    subOutputList = []
    for i in yearNestList:
        i.insert(1,insertListElement)
        subOutputList.append(str.join('\n',i))
    outputString = str.join('\n\n',subOutputList)
    return outputString
    
    

#print(construct_cal_year(2015))




def print_space_display_calendar(calendar):
    temp=calendar.replace(' ','*')
    return temp.replace('\n','+\n')

ans = display_calendar(2015)
print('START')
print(print_space_display_calendar(ans))
print('END')








def isLeapYear(year) :
    if((year % 4) == 0) :
        if ((year % 100) == 0) :
            if ((year % 400) == 0) :
                return True
            else :
                return False
        else :
            return True
    else :
        return False

def dayOfYear(date):
    mlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = date.split("-")
    day = int(date[2])
    mon = int(date[1])
    year = int(date[0])
    for i in range(mon-1):
        day+=mlist[i]
    if mon > 2:
        if((year % 4) == 0) :
            if ((year % 100) == 0) :
                if ((year % 400) == 0) :
                    day+=1
            else :
                day+=1
                    
         
    return day
date = "2004-03-01"
print(dayOfYear(date))
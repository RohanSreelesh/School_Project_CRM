def datecheck(date):
    import time
    today=time.strftime("%d%m%Y",time.gmtime())
    date=str(date)
    day=int(date[0:2])
    month=int(date[2:4])
    year=int(date[4:])
    #alphabet check
    for i in date:
        if i not in '1234567890':
            return False
            break
    if len(date)!=8:  #underflow/overflow check
        return False

    days=[31,28,31,30,31,30,31,31,30,31,30,31]

    months=[1,2,3,4,5,6,7,8,9,10,11,12]

    if day>31 or day <0 or month>12 or month<0:
        #invalid month,day
        print('wrong month or day out of range')
        return False

    #month corresponding day
    if day>days[month-1]:
        print('enter corresponding correct date')
        return False




    #future date check
    aajkadin=int(today[:2])
    tomonth=int(today[2:4])
    toyear=int(today[4:])

    if year>toyear:
        return True
    elif year==toyear:
        if month>=tomonth:
            if day>=aajkadin:
                return True
            else:
                print('correct year and month wrong day')
                return False
        else:
            print('correct year wrong month')
            return False

    else:

        print('cannot be past date unless you can time travel')
        return False
'''
x=''

while x!='q':
    x=input("énter date")
    print(datecheck(x))

'''
def LeapYear(y):
    ans = True
    if(y%4==0):
        if(y%100==0):
            ans = False
            if(y%400==0):
                ans = True
        else:
            ans = True
    else:
        ans = False
    return ans

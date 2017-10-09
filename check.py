def LeapYear(y):
    ans = False
    if y%4==0 :
        if y%100!=0 or y%400==0:
            ans = True
    return ans

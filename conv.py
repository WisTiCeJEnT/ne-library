def intStr(n):
    n = str(n)
    dic = {'1':"one" , '2':"two" , 
        '3':"three" , '4':"four" , 
        '5':"five" , '6':"six" , 
        '7':"seven" , '8':"eight" , 
        '9':"nine" , '0':"zero"}
    if n in dic:
        return dic[n]
    return "conv.intStr.ERROR"

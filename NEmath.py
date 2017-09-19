def plist(n):
    pls = []
    ls = list(range(n))
    for i in range(2,int(n**0.5)+1):
        if ls[i]:
            for dele in range(i+i,n,i):
                ls[dele] = False
    for i in range(2,n):
        if ls[i]:
            pls.append(i)
    return pls          #return list of prime

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)

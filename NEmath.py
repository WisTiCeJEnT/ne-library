def plist(n):
    pls = []
    n += 1
    ls = list(range(n))
    for i in range(2,int(n**0.5)+1):
        if ls[i]:
            for dele in range(i+i,n,i):
                ls[dele] = False
    for i in range(2,n):
        if ls[i]:
            pls.append(i)
    return pls          #return list of prime

def isPrime(n):
    pls = plist(n//2)
    for i in pls:
        if n%i==0:
            return False
    return True

def isPalin(n):
    n = str(n)
    if n==n[::-1]:
        return True
    return False

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)

import requests
import math
from fractions import gcd

def egcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def getd(a, m):
    '''
     Function to generate modular inverse
    '''
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def is_prime(n):
    '''
     Function to check for primality
    '''
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1
    for divisor in xrange(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def keygen():
    '''
    Function to generate RSA key pair
    '''
    p = q = 3
    while p == q:
        p = int(requests.get("https://www.random.org/integers/?num=1&min=1&max=31621&col=1&base=10&format=plain&rnd=new").content)
        q = int(requests.get("https://www.random.org/integers/?num=1&min=1&max=31621&col=1&base=10&format=plain&rnd=new").content)
        p += not(p&1)                             # changes the values from
        q += not(q&1)                             # even to odd

        while is_prime(p) == False:               #checks for primality
            p -= 2
        while is_prime(q) == False:
            q -= 2
    n = p * q
    tot = (p-1) * (q-1)
    e = tot
    while gcd(tot,e) != 1:
        e = int(requests.get("https://www.random.org/integers/?num=1&min=1&max=" +str(tot-1)+"&col=1&base=10&format=plain&rnd=new").content)
    d = getd(tot,e)                       # gets the multiplicative inverse
    while d<0:                            # i can probably replace this with mod
        d = d + tot
    print "Public key is: "+str(e)
    print "private key is: "+str(d)
    print  "Generated  modulus is: "+str(n)


if __name__ == "__main__":
    keygen()
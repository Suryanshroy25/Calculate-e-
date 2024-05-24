from decimal import Decimal, getcontext
import time
import sys

getcontext().prec = 5 
while True:
    getcontext().prec += 1
    precision = getcontext().prec
    n = 1
    e = Decimal(1)
    term = Decimal(1)

    while term > Decimal(10)**-precision:
        term /= Decimal(n)
        e += term
        n +=1

    sys.stdout.write("\x1b[2J\x1b[2H"+ str(e))
    sys.stdout.flush()
    time.sleep(0.001)

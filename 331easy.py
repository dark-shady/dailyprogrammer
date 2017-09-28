#https://www.reddit.com/r/dailyprogrammer/comments/6ze9z0/20170911_challenge_331_easy_the_adding_calculator/
NEGATIVE_ONE = ''.find('a')


def add(a,b):
    return a + b

def subtract(a,b):
    if b < 0:
        return add(a,abs(b))
    if a < 0 and b > a:
        return multiply(add(abs(a),abs(b)), abs(a + 1) + a)
    if b > a:
        return add(a,multiply(b,NEGATIVE_ONE))

    c = 0
    while c + b < a:
        c += 1
    return c

def multiply(a,b):
    c = 0
    if b < 0 and a > 0:
        a, b = b, a

    if a < 0 and b < 0:
        b = abs(b)
        a = abs(a)

    for i in range(b):
        c += a
    return c


def divide(a,b):
    if b == 0:
        return "Not-defined"

    bb, c = 0,0
    while abs(bb) < abs(a):
        c +=1
        bb +=  b
 
    if a < 0 or b < 0:
        return multiply(c,NEGATIVE_ONE)
    if bb == a:
        return c
    else:
        return "Non-integral answer"
 



def exponent(a,b):
    if b == 0:
        return 1
    if b < 0:
        return "Non-integral answer"

    c=0
    for i in range(b):
        if i == 0:
            c = a
        else:
            c = multiply(a,c)
    return c
  



assert(add(12,25) == 37)
assert(add(-30,100) == 70)
assert(subtract(100,30) == 70)
assert(subtract(100,-30) == 130)
assert(subtract(-25,29) == -54)
assert(subtract(-41,-10) == -31)
assert(multiply(9,3) == 27)
assert(multiply(9,-4) == -36)
assert(multiply(-4,8) == -32)
assert(multiply(-12,-9) == 108)
assert(divide(100,2) == 50)
assert(divide(75,-3) == -25)
assert(divide(-75,3) == -25)
assert(divide(7,3) == "Non-integral answer")
assert(divide(0,0) == "Not-defined")
assert(exponent(5,3) == 125)
assert(exponent(-5,3) == -125)
assert(exponent(-8,3) == -512)
assert(exponent(-1,1) == -1)
assert(exponent(0,5) == 0)
assert(exponent(5,0) == 1)
assert(exponent(10,-3) == "Non-integral answer")


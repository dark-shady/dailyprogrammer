#https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/

import math

def is_prime(num):
    if num & 0x01 == 0 or num % 5 == 0: return False
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 5 == 0:
        return False
    else:
        for i in range(2,int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True



def find_primes(input_num):
    if is_prime(input_num):
        print("{} is prime".format(input_num))
    else:
        lower = upper = input_num
        while not is_prime(lower):
            lower -= 1
        while not is_prime(upper):
            upper += 1
        print ("{} < {} < {}".format(lower, input_num, upper))

find_primes(270)
find_primes(541)
find_primes(993)
find_primes(649)

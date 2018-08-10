# https://old.reddit.com/r/dailyprogrammer/comments/8xbxi9/20180709_challenge_365_easy_uparrow_notation/

def up_arrow(base, number_of_arrows, exp):
    # Base case
    if number_of_arrows == 1:
        return base ** exp
    #Set original result to base
    result = base

    # Iterate exp - 1 times.  Each time recursively step through until number_of_arrows reaches base case.
    # Then update result and use it for next iteration. Repeat recursion.
    for _ in range(exp - 1):
        result = up_arrow(base, number_of_arrows - 1, result)
    return result


print(up_arrow(-1,3,3))
print(up_arrow(1,1,0))
print(up_arrow(1,2,0))

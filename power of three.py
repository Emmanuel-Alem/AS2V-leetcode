
import math
def isPowerOfThree(n):
    if n <= 0:
        return 'false'
    elif math.log(n,3) < 0:
        return 'false'
    else:
        return 'true'



print(isPowerOfThree(-1))

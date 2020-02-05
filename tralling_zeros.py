import math
import time
def zeros(n):
    count = 0
    if n<5:
        return 0
    for i in range(5, n+1, 5):
        temp = math.log(i, 5)
        if abs(temp - int(temp)<0.001):
            count += int(temp)
        else:
            count += 1
    return count

def zeros3(n):
    total = 0
    while True:
        n = n//5
        if n < 5:
            return total
        total += n
print(zeros3(100))
enumerate

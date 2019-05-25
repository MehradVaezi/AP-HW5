import math
import random

def IsInCircle(x, y):
    return (math.sqrt(x**2 + y**2) < 0.5)

def Find():
    N = 0
    P = 3.0
    inside = 0
    while (abs(math.pi - P) > 0.01):
        N += 1
        a = random.uniform(0, 0.5)
        b = random.uniform(0, 0.5)
        inside += IsInCircle(a, b)
        P = (inside*4)/N
    print("Minimum number of random points needed: ", N)
    return P

n = int(input("How many times should I run Find() ? "))

pi_sum = 0
for i in range(n):
    pi_sum += Find()
pi_sum = pi_sum / n

print("PI is approximately ->", format(pi_sum, '.5f'))
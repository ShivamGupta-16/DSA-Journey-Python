# Q. Given an integer n, find the maximum power of two that is smaller than n.

def maximum_power(n):
    if n<=1:
        return 0
    
    power = 0
    while (1<<power) < n:
        power+=1
    
    return 1<<(power-1)

print(maximum_power(100))
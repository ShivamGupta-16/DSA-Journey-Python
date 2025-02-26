def fact(x):
    if x ==0:   #base case
        return 1
    else:
        return x*fact(x-1)
    
    
print(fact(5))
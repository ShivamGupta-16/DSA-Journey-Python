def print2n(n):
    if n>0:
        print(n)
        print2n(n-1)
print2n(9)
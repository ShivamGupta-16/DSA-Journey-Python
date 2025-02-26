def sumof(arr,n):
    if n==0:
        return 0
    else:
        return sumof(arr,n-1) + arr[n-1]
arr=[3,2]
print(sumof(arr,len(arr)))
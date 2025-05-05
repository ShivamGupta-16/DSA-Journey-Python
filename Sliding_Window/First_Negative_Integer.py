arr = [-1,2,-3,-4,34,5,-3,-4,-5,9,10,11]
k = 3

FNI = 0
for i in range(k-1, len(arr)):
    while FNI < i and (FNI <= i-k or arr[FNI] >=0):
        FNI+=1
    if FNI <= i and arr[FNI] < 0:
        print(arr[FNI])
    else:
        print(0)

        
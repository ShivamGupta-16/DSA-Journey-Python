
def insert(arr):
    for i in range(len(arr)):
        key = arr[i]
        j =i-1
        while j>=0 and key<arr[j]:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1] = key
    print(arr)

arr = [232,24,23,43,43,343,24234,2423]
arr= [12,81,7,6,5,4,3,2,1]
insert(arr)
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
arr= [4223,4324,23,42,34,23,4,2,34,32,4,3,4,4,23,23]
bubble(arr)

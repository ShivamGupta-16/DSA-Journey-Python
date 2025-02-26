def lin(arr, x):
    for i in range(len(arr)):
        s=0
        if arr[i] == x:
            s=1
            break
    if s!=1:
        print("number is not in the list.")
    else:
        print(i)

arr= [3,324,34,56,234,30,33,4,37,324,39,2,4,23,23,54,6,5,76,8,7,879,8988]
x = 34
lin(arr,x)
# lin([1,2,3,4,44,54,556,22], 44)g
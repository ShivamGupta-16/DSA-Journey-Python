def bin(arr,target):
    low=0
    high=len(arr)-1
    c=0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]== target:
            c=1
            print("number is at index:",mid)
            break

        elif arr[mid]> target:
            high= mid-1
        else:
            low = mid+1
    if c==0:
        print("Number is not present in the list.")

arr= [3,324,34,56,234,30,33,43,32,34,34,43]
target = 30
bin(arr,target)
bin([1,2,3,4,44,54,556,22], 44)

# steps to do :
# 1. Use two Pointer High and Low
# 2. calculate mid
# 3. Compare middle element with target
# 4. Update Search Space
    

# Leetcode Question - 704
        


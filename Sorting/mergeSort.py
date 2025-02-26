def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right= arr[mid:]
        mergesort(left)
        mergesort(right)
        # print(arr)
        return merge(arr,left,right)
def merge(arr, left, right):
    i,j,k=0,0,0
    while i< len(left) and j<len(right):
        if left[i]< right[j]:
            arr[k]= left[i]
            i+=1
        else:
            arr[k]= right[j]
            j+=1
        k+=1
    
    while i< len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j< len(right):
        arr[k]= right[j]
        j+=1
        k+=1
    # print(arr)
    return arr
arr= [2,3,1,4,6,7,2]
print(mergesort(arr))
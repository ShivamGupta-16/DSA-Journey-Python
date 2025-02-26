def cycle_sort(arr):
    for cyclestart in range(len(arr)-1):
        item = arr[cyclestart]
        pos= cyclestart

        for i in range(cyclestart+1,len(arr)):
            if arr[i]<item:
                pos+=1

        if pos ==cyclestart:
            continue

        while item ==arr[pos]:
            pos+=1

        arr[pos], item = item, arr[pos]

        while pos!= cyclestart:
            pos= cyclestart
            for i in range(cyclestart+1, len(arr)):
                if arr[i]< item:
                    pos+=1

            while item ==arr[pos]:
                pos+=1
            arr[pos],item = item, arr[pos]


arr= [3,44,3,3,3,3,22,11]
print(cycle_sort(arr),arr)
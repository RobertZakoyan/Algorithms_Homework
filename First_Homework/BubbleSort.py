def BubbleSort(arr):
    swapped = False 
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j+1], arr[j] = arr[j], arr[j+1]
        if not swapped:
            break
    return arr
print(BubbleSort([4,1,4,1,888,0,0,-1]))

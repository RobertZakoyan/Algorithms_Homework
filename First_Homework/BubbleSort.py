def BuubleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
print(BuubleSort([4,1,4,1,888,0,0,-1]))
def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while (j >-1 and array[j] > key):
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array

print(InsertionSort([2,3,1,1,6,1,1,1]))
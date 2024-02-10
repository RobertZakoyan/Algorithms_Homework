def selectionSort(array):
    for index in range(len(array)-1):
        min_index = index
        for j in  range(index+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != index: 
            array[min_index], array[index] = array[index], array[min_index] 
    return array
print(selectionSort([1,4,4,6,0,-1]))

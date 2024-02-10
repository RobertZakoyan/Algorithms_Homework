def selectionSort(array):
    for index in range(len(array)):
        min_index = index
        for j in  range(index+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[index] = array[index], array[min_index] 
    return array
print(selectionSort([1,4,4,6,0,-1]))
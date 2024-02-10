def BinarySearch_Normal(arr,  target):
    lower = 0
    higher = len(arr)
    while higher >= lower:
        mid = (higher + lower) //2
        if arr[mid] == target:
            return mid,arr[mid]
        if arr[mid] > target:
            higher = mid
        if arr[mid] < target:
            lower = mid
print(BinarySearch_Normal([0,1,2,3,4,5,6,99,204], 99))

def BinarySearch_Recursive(arr,target):
    lower = 0
    higher = len(arr)
    mid = (lower+higher)//2
    if arr[mid] == target:
        return mid, arr[mid]
    if arr[mid] > target:
        return BinarySearch_Recursive(arr[:mid-1], target)
    else:
        return BinarySearch_Recursive(arr[mid+1:], target)
print(BinarySearch_Recursive([0,1,2,3],0))
# binary serach 
# 반으로 짤라서 찾아본다

# Iterative binary serach
def binary_itr(arr, start, end, target):
    while start <= end:

        mid = (start + end) //2 
        if arr[mid] < target:
            start = mid + 1
        
        elif arr[mid] > target:
            end = mid -1

        else:
            return mid
    
    return -1 

arr = [ 2, 5, 8, 10 ,16, 22, 25]

target = 10

result = binary_itr(arr, 0, len(arr) -1, target)

if result != -1:
    print("Element is presetn at index %d" %result)

else:
    print("Element is not present in array")


# Recursive Binary Search 

def binary_recur(arr, start, end, target):
    if end >= start:

        mid = start + end//2

        if arr[mid] < target:
            binary_recur(arr, mid+1, end, target)
        
        elif arr[mid] > target:
            binary_recur(arr, mid-1, end, target)

        else:
            return -1

arr = [ 2, 5, 8, 10 ,16, 22, 25]

target = 10

result = binary_itr(arr, 0, len(arr) -1, target)

if result != -1:
    print("Element is presetn at index %d" %result)

else:
    print("Element is not present in array")
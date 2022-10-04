# Linear Search

def search(arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i

arr = [2, 5, 7, 9, 10, 16, 22]
target = 10

print(search(arr, target))
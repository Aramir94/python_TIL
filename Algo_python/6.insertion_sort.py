# sorted array and un sorted array split 
# small data 좋아효.


def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j -1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i +1] = key
    return A

A = [5, 2, 4, 6, 1, 3]
print(insert_sort(A))

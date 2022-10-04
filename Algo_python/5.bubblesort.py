# simple algorism
# 대부분 소팅 되어있는 어레이 다룰때 매우 좋아..요

def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iterations += 1

            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(bubble_optimized(A))
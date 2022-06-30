def maxHeapify(A, i):
    e = 2*i
    d = 2*i + 1
    if e <= A.length and A[e] > A[i]:
        maior = e
    else:
        maior = i
    if d <= A.length and A[d] > A[maior]:
        maior = d
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        maxHeapify(A, maior)

def buildHeap(A):
    heapSize = len(A)-1
    for i in range(heapSize//2, -1, -1):
        maxHeapify(A, i)



 # -- Main --
 A = [4, 1, 3, 2, 16, 9, 10, 14 , 8, 7 ]
 print(A)
 buildHeap(A)
 print(A)
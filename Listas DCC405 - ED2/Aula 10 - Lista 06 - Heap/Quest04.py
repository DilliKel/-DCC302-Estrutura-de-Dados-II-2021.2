import time

# -- Percorrer o Array --
def left(index):
    return 2 * index + 1

def right(index):
    return 2 * (index + 2)

def parent(index):
    return index - 1 // 2

def getLastNonLeaf(n):
    return n // 2 - 1

def heapify(arr, i):
    n = len(arr)
    bignum = i 
    if left(i) < n and arr[left(i)] > arr[bignum]:
        bignum = left(i)

    if right(i) < n and arr[right(i)] > arr[bignum]:
        bignum = right(i)

    if bignum != i:
        arr[i], arr[bignum] = arr[bignum], arr[i]

        heapify(arr, bignum)

def buildHeap(arr):
    n = len(arr)
    startIdx = getLastNonLeaf(n) 


    for i in range(startIdx, -1, -1):
        heapify(arr, i)

def printHeap(arr):
    n = len(arr)
    print("A representação do Heap é:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def isHeap(arr, i, n):
    if (i >= (n - 2) / 2):
        return True
    if arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2] and isHeap(arr, 2 * i + 1, n) and isHeap(arr, 2 * i + 2, n):
        return True

    return False

# -- A Main --

arr = [70, 80, 50, 27, 18]
n = len(arr)
print('O Array sem a aplicação do buildHeap')
print(arr)
time.sleep(1)
print('O array inicial é um heap?')
print(isHeap(arr, 0, n))
time.sleep(1)
print('')
buildHeap(arr)
printHeap(arr)
time.sleep(1)
print('O array após a aplicação do buildHeap é um heap?')
print(isHeap(arr, 0, n))
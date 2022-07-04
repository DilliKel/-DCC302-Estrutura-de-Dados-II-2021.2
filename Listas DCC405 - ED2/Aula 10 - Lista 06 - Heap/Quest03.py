# Comparar se o vetor armazenado dentro do Array é um Max Heap, se for ele printa True, Se não for printa false

def MaxHeap(array):
    n = len(array)
    for i in range(n):
        m = i * 2
        num = array[i]
        if m + 1 < n:
            if num < array[m + 1]:
                return False
        if m + 2 < n:
            if num < array[m + 2]:
                return False
    return True
array = [100, 40, 30, 20, 15]       #true
#array = [10, 400, 300, 200, 150]   #false


print(MaxHeap(array))
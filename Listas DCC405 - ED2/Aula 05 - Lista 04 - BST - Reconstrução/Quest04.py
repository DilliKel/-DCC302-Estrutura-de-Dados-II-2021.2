import queue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
    return root

def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.value == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.value
        deleteDeepest(root, temp)
        key_node.value = x
    return root

# PERCURSOS EM PROFUNDADE (DFS)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value, end=" ")
        inOrder(root.right)

def preOrdem(root):
    if root:
        print(root.value, end=" ")
        preOrdem(root.left)
        preOrdem(root.right)

def posOrdem(root):
    if root:
        posOrdem(root.left)
        posOrdem(root.right)
        print(root.value, end = " ")      

def printTree(root, level=0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4 * level + '-> ' + str(root.value))
        printTree(root.left, level+1)

def findMin(root):
    if root is None:
        return None
    while root.left != None:
        root = root.left
    return root

def findMax(root):
    if root is None:
        return None
    while root.right != None:
        root = root.right
    return root

def findHeight(root):
    if root is None:
        return -1
    leftH = findHeight(root.left)
    rightH = findHeight(root.right)
    return max(leftH, rightH) + 1

# Percurso em Level (BFS)
q = queue.Queue()

def deleteNode(root, value):
    if root is None:
        return None
    elif value < root.value:
        root.left = deleteNode(root.left, value)
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    else:  # Nó foi encontrado
        # Caso 1: Nó folha
        if root.left and root.right is None:
            root = None
        # Caso 2: Nó tem um filho
        elif root.left is None:
            temp = root
            root = root.right
            temp = None
        elif root.right is None:
            temp = root
            root = root.left
            temp = None
        # Caso 3: Nó tem dois filhos
        else:
            minNode = findMin(root.right)
            root.value = minNode.value
            root.right = deleteNode(root.right, minNode.value)
    return root

def levelOrder(root):
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        current = q.queue[0]
        print(current.value, end=" ")
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)
        q.get()

# Main (Definindo a árvore)
root = None
root = insert(root, 15)
root = insert(root, 6)
root = insert(root, 18)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 17)
root = insert(root, 20)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 13)
root = insert(root, 9)


# Imprimindo tudo

print("\n--------------------------------------------------------")
printTree(root)
print("\n--------------------------------------------------------")
print('min: ', findMin(root).value)
print('max: ', findMax(root).value)
print('height: ', findHeight(root))
print("--------------------------------------------------------")
print('preOrdem: ')
preOrdem(root)
print("\n--------------------------------------------------------")
print('inOrder: ')
inOrder(root)
print("\n--------------------------------------------------------")
print('posOrdem: ')
posOrdem(root)
print("\n--------------------------------------------------------")
deleteNode(root, 20)
print("Árvore pos remoção:")
printTree(root)
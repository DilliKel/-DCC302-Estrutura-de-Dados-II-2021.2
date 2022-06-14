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

def posOrder(root):
    if root:
        posOrder(root.left)
        posOrder(root.right)
        print(root.value, end=" ")

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value, end=" ")
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.value, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def printTree(root, level=0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4 * level + '-> ' + str(root.value))
        printTree(root.left, level+1)

# Main
root = None

root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 6)


printTree(root)
print('---------------------------------------------------')
print('preOrder', preOrder(root))
print('---------------------------------------------------')
print('inOrder', inOrder(root))
print('---------------------------------------------------')
print('posOrder', posOrder(root))
print('---------------------------------------------------')
#print('levelOrder', levelOrder(root))

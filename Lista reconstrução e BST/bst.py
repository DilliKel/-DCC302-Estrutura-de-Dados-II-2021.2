### ----- ÁRVORE DE BUSCA BINÁRIA  ----- ###

# Estrutura do nó
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
  

# PERCURSOS EM PROFUNDIDADE (DFS)
def preOrdem(root):
  if root:
    print(root.value, end=" ")
    preOrdem(root.left)
    preOrdem(root.right)

def inOrdem(root):
  if root:
    inOrdem(root.left)
    print(root.value, end=" ")
    inOrdem(root.right)

def posOrdem(root):
  if root:
    posOrdem(root.left)
    posOrdem(root.right)
    print(root.value, end=" ")
    

# PERCURSOS EM LARGURA (BFS)  
import queue
q = queue.Queue()

def levelOrder(root):
  if root is None: return None
  q.put(root)
  while not q.empty():
    current = q.queue[0]
    print(current.value, end=" ")
    if current.left is not None: q.put(current.left)
    if current.right is not None: q.put(current.right)
    q.get() 

# Função para imprimir mais "bonitinho"
def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' *4*level + '->' +str(root.value))
    printTree(root.left, level+1)

# Outras funções    
def findMin(root):
  if root is None:
    return None
  while root.left != None:
    root = root.left
  return root.value
  
def findMax(root):
  if root is None:
    return None
  while root.right != None:
    root = root.right
  return root.value

def findHeight(root):
  if root is None:
    return -1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

   
# ------ Main --------
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

# preOrdem(root)
printTree(root)
print("Min: ",findMin(root))
print("Max: ",findMax(root))
print("Altura: ",findHeight(root))
levelOrder(root)
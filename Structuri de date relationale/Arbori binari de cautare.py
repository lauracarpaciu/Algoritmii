class BSTNode:
    def __init__(self,value):
        self.value=value
    left=None
    right=None

numbers=[33,2,15,43,100,50,22,3,14]
root= BSTNode(numbers[0])

def addNumberToTree(value,tree):
      if value<=tree.value:
        if tree.left==None:
            tree.left=BSTNode(value)
        else:
            addNumberToTree(value,tree.left)
      else:
        if tree.right==None:
            tree.right=BSTNode(value)
        else:
            addNumberToTree(value,tree.right)



for index in range(1,len(numbers)):
     addNumberToTree(numbers[index],root)


def printAscendingOrder(tree=None):

   if tree==None:
       return

   printAscendingOrder(tree.left)
   print(tree.value)

   printAscendingOrder(tree.right)


printAscendingOrder(root)
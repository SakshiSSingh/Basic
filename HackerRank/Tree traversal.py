class Tree:
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None


def preOrder(tree):
    if tree:
        print(tree.root)
        preOrder(tree.left)
        preOrder(tree.right)

def postOrder(tree):
    if tree:
        postOrder(tree.left)
        postOrder(tree.right)
        print(tree.root)

def inOrder(tree):
    if tree:
        inOrder(tree.left)
        print(tree.root)
        inOrder(tree.right)

Tree1 = Tree(1)
Tree1.left = Tree(2)
Tree1.right = Tree(3)
Tree1.left.left = Tree(4)
Tree1.left.right = Tree(5)

preOrder(Tree1)
print('\n')
postOrder(Tree1)
print('\n')
inOrder(Tree1)

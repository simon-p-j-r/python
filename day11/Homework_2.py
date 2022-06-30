# 小彭的乱码
class Node:
    def __init__(self, num, lchild=None, rchild=None):
        self.num = num
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self):
        self.root = None
        self.list_help = []

    def addnode(self, node: Node):
        self.list_help.append(node)
        if self.root is None:
            self.root = self.list_help[0]
        elif self.list_help[0].lchild is None:
            self.list_help[0].lchild = node
        else:
            self.list_help[0].rchild = node
            self.list_help.pop(0)

    def preolder(self, root: Node):
        if root is None:
            return
        print(root.num)
        self.preolder(root.lchild)
        self.preolder(root.rchild)

    def midolder(self, root):
        if root is None:
            return
        self.preolder(root.lchild)
        print(root.num)
        self.preolder(root.rchild)

    def lastolder(self, root):
        if root is None:
            return
        self.preolder(root.lchild)
        self.preolder(root.rchild)
        print(root.num)


node_one = Node(1)
tree = Tree()
tree.addnode(node_one)
tree.preolder(tree.root)

#coding:utf-8

"""
二叉树实现
"""

class Node(object):
    """树节点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    """implement for Tree."""
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        #当根节点为空时
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild != None:
                queue.append(cur_node.lchild)
            if cur_node.rchild != None:
                queue.append(cur_node.rchild)


    def preorder(self,node):
        """先序遍历"""
        if node == None:
            return
        print(node.elem,end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        """中序遍历"""
        if node == None:
            return
        self.preorder(node.lchild)
        print(node.elem,end=" ")
        self.preorder(node.rchild)

    def postorder(self,node):
        """后序遍历"""
        if node == None:
            return
        self.preorder(node.lchild)
        self.preorder(node.rchild)
        print(node.elem,end=" ")


if __name__ == "__main__":
    tree = Tree()
    for value in range(18):
        tree.add(value)

    #tree.breadth_travel()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()

class Node:
    """represent a node of binary search tree"""
    def _init_(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

class BSTtree:
    def _init_(self,root=None,size=0):
        self.root=root
        self.size=size

    def insert(self,add_node):
        add_node=Node()
        compareNode=None
        if self.root is None:
            self.root=add_node
        else:
            compareNode=self.root
            while True:
                if add_node.key>compareNode.key:
                    compareNode=compareNode.right
                else:
                    compareNode = compareNode.left

        parentNode=compareNode
        if add_node.key>parentNode.key:
            parentNode.right=add_node
        else:
            parentNode.left=add_node


    def max(self,rootnode):
        max=None
        current=rootnode
        while rootnode.right is not None:
            current=current.right
        current=current
        max=current

    def min(self,rootnode):
        min=None
        current=rootnode
        while rootnode.left is not None:
            current=current.left
        current=current
        min=current

    def find(self,find_node):
        find_node=Node()
        parent=None
        current=self.root
        while current is not None:
            if find_node.key<current.key:
                current=current.left
            elif find_node.key>current.key:
                current = current.right
            else:
                break
        current=current
        if current is not None:
            return True
        else:
            return False

    def delete(self,delete_node):
        delete_node=Node()
        found_node=delete_node
        if self.find(found_node)==True:
            replace_foundnode=self.max(found_node.left)
            if replace_foundnode!=found_node:
                found_node.left.parent=replace_foundnode
                found_node.right.parent = replace_foundnode
                replace_foundnode.parent.right=None
            else:
                found_node.parent.left=found_node.left
        else:
            print("sorry, you value has nor been found yet")

    def inorder(self,rootnode):
        self._inorder(rootnode)
    def _inorder(self,rootnode):
        if not rootnode:
            return
        self._inorder(rootnode.left)
        print(rootnode.key)
        self._inorder(rootnode.right)

    def preorder(self,rootnode):
        self._preorder(rootnode)
    def _preorder(self,rootnode):
        if not rootnode:
            return
        print(rootnode.key)
        self._preorder(rootnode.left)
        self._preorder(rootnode.right)

    def postorder(self,rootnode):
        self._postorder(rootnode)
    def _postorder(self,rootnode):
        if not rootnode:
            return
        self._preorder(rootnode.left)
        self._postorder(rootnode.right)
        print(rootnode.key)
    def height(self,rootnode):
        self._height(rootnode)
    def _height(self,rootnode):
        if not rootnode:
            return -1
        left_height=self._height(rootnode.left)
        right_height=self._height(rootnode.right)
        return 1+left_height+right_height

    def count(self):
        return self._count(self.root)
    def _count(self,root):
        if not root:
            return 0
        return 1+self._count(root.left)+self._count(root.right)

    def main(self):
        import random
        test=BSTtree()
        for i in random.sample([j for j in range(1,100)],5):
            test.insert(i)
        print("insert:")
        test.insert(78)
        test.insert(101)
        test.insert(74)

        test.preorder(test.root)
        test.inorder(test.root)
        test.postorder(test.root)

        print("height:")
        print(test.height(test.root))
        print("min")
        print(test.min(test.root))

        print("delete:")
        test.delete(101)
        test.delete(12)

    if __name__=='__main__':
        main()

















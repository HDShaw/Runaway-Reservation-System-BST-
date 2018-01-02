class tree_node(object):
    def __init__(self,key = None, left = None, right = None):
        self.key=key
        self.left=left
        self.right=right
class binary_search_tree(object):
    def __init__(self,root=None):
        self.root=root

    def insert(self,key):
        """recursion way"""
        self.root=self._insert(self.root, key)
    def _insert(self,root,key):
        if not root:
            root=tree_node(key)
        else:
            if key<root.key:
                root.left=self._insert(root.left,key)
            elif key>root.key:
                root.right=self._insert(root.right,key)
            else:
                print(key+"is already in tree")

        return root
    def delete(self,key):
        self._delete(self.root,key)
    def _delete(self,root,key):
        if not root:
            print("the bianry search tree does not exit")
            return
        else:
            if key<root.key:
                root.left=self._delete(root.left,key)
            elif key>root.key:
                root.right=self._delete(root.right,key)
            elif root.left and root.right:
                right_min=self._find_min(root)
                root.key=right_min.key
                root.right=self._delete(root.right,right_min.key)
            elif root.left:
                root=root.left
            elif root.right:
                root=root.right
            else:
                root=None
            return root
    def find_min(self):
        return self._find_min(self.root)
    def _find_min(self,root):
        if not root.left:
            return root
        return self._find_min(root.left)
    def find_max(self):
        return self._find_max(self.root)
    def _find_max(self,root):
        if not root.right:
            return root
        return self._find_max(root.right)
    def find(self,key):
        return self._find(self.root,key)
    def _find(self,root,key):
        if not root:
            print("sorry, the node is not found")
            return
        if key<root.key:
            return self._find(root.left,key)
        elif key>root.key:
            return self._find(root.right,key)
        else:
            print("the node is found")
            return root

    def height(self):
        return self._height(self.root)
    def _height(self,root):
        if not root:
            return -1
        left_height=self._height(root.left)
        right_height=self._height(root.right)
        if left_height>right_height:
            return 1+left_height
        else:
            return 1+right_height
    def subtree(self):
        return self._subtree(self.root)
    def _subtree(self,root):
        if not root:
            return 0
        left_subtree=self._subtree(root.left)
        right_subtree=self._subtree(root.right)
        return 1+left_subtree+right_subtree
    def inorder(self):
        return self._inorder(self.root)
    def _inorder(self,root):
        if not root:
            return
        self._inorder(root.left)
        print(root.key)
        self._inorder(root.right)
    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self,root):
        if not root:
            return
        print(root.key)
        self._preorder(root.left)
        self._preorder(root.right)
    def postorder(self):
        return self._postorder(self.root)
    def _postorder(self,root):
        if not root:
            return
        self._postorder(root.left)
        self._postorder(root.right)
        print(root.key)


def main():
    import random
    test = binary_search_tree()
    print(type(test))
    for i in random.sample([j for j in range(1, 100)], 5):
        test.insert(i)
    print('insert: ')
    test.insert(78)
    test.insert(101)
    test.insert(14)

    test.preorder()
    test.inorder()
    test.postorder()
    print('height: ', test.height())
    print('count: ', test.subtree())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)

    print( 'delete: ')
    test.delete(101)
    test.delete(12)

    test.preorder()
    test.inorder()
    test.postorder()

    test.find(71)

    test.find(78)

    print('height: ', test.height())
    print('count: ', test.subtree())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)



if __name__ == '__main__':
    main()









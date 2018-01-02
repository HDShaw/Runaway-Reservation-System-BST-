class AVLtree:
    def insert(self,key):
        self.root=self._insert(self.root,key)
    def _insert(self,root,key):
        if not root:
            root=AVLtreeNode(key=key)
        else:
            if AVLtreeNode.key>key:
                directtion=0
            else:
                directtion = 1


import sys
sys.stdin = open('/Users/mayank/Development/Coding Env/4. PYTHON/input.txt', 'r')
sys.stdout = open('/Users/mayank/Development/Coding Env/4. PYTHON/output.txt', 'w')

'''
Applications of BST :
1. to implement set data structure
2. to sort the data(using inorder traversal)
3. to have better performance in searching, inserting and deleting, all with O(logn) time complexity.
'''

'''
1. The size of a binary tree refers to the number of nodes it has. The distance from a node B to the root node is the level of B. The sum of the levels of each of the external nodes in a tree is called the external path length. The maximum level, among all of the external nodes, is called the height of the tree.

2. The maximum number of nodes at level ‘l’ of a binary tree is 2^l.
3. Level: The level of a node is the number of connections from the root node. The root node is at level 0. Nodes B and C are at level 1.
4. Height of a tree: This is the number of levels in a tree. Our tree has a height of 4.
5. Depth: The depth of a node is the number of edges from the root of the tree to that node. The depth of node H is 2.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val, None, None)

        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val, None, None)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = Node(val, None, None)
            else:
                self._insert(node.right, val)

    def find_min(self):
        if self.root is None:
            return
        return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is None:
            return node.val
        return self._find_min(node.left)

    def inorder(self):
        '''
        Inorder traversal
        left->root->right
        '''
        if self.root is None:
            return 'No data to show'
        else:
            return self._inorder(self.root)

    def _inorder(self, node):
        if node.left:
            self._inorder(node.left)
        print(node.val, end=" ")
        if node.right:
            self._inorder(node.right)

    def preorder(self):
        '''
        Preorder traversal
        root->left->right
        '''
        if self.root is None:
            return 'No data to show'
        else:
            return self._preorder(self.root)

    def _preorder(self, node):
        print(node.val, end=" ")
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)

    def postorder(self):
        '''
        Postorder traversal
        left->right->root
        '''
        if self.root is None:
            return 'No data to show'
        else:
            return self._postorder(self.root)

    def _postorder(self, node):
        if node.left:
            self._postorder(node.left)
        if node.right:
            self._postorder(node.right)
        print(node.val, end=" ")

    def levelorder(self):
        if self.root is None:
            return 'No data to show'
        else:
            return self._levelorder(self.root)

    def _levelorder(self, node):
        q = []
        q.append(node)
        while len(q) > 0:
            node1 = q.pop(0)
            print(node1.val, end=" ")
            if node1.left:
                q.append(node1.left)
            if node1.right:
                q.append(node1.right)

    def reverse_levelorder(self):
        if self.root is None:
            return
        q = []
        s = []
        q.append(self.root)
        while len(q) > 0:
            node = q.pop(0)
            s.append(node)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        while len(s) > 0:
            node = s.pop()
            print(node.val, end=" ")

    def inorder_using_stack(self):
        if self.root is None:
            return
        s = []
        curr = self.root
        while True:
            if curr is not None:
                s.append(curr)
                curr = curr.left
            elif s:
                node = s.pop()
                print(node.val, end=" ")
                curr = node.right
            else:
                break

    def right_view(self):
        ans = []
        level = []
        q = [self.root]
        while q != []:
            for node in q:
                if node and node.left:
                    level.append(node.left)
                if node and node.right:
                    level.append(node.right)
            ans.append(node)
            q = level
            level = []
        for node in ans:
            print(node.val, end=" ")

    def left_view(self):
        ans = []
        level = []
        q = [self.root]
        while q != []:
            for node in q:
                if node and node.right:
                    level.append(node.right)
                if node and node.left:
                    level.append(node.left)
            ans.append(node)
            q = level
            level = []
        for node in ans:
            print(node.val, end=" ")


bt = BST()
bt.insert(10)
bt.insert(2)
bt.insert(3)
# bt.insert(7)
# bt.insert(8)
bt.insert(15)
bt.insert(12)
bt.insert(14)
bt.right_view()
print("Right view")
bt.left_view()
print("Left view")
bt.inorder()
print("InOrder")
bt.preorder()
print("PreOrder")
bt.postorder()
print("PostOrder")
bt.levelorder()
print("LevelOrder")
bt.reverse_levelorder()
print("ReverseLevelOrder")
bt.inorder_using_stack()
print("InOrderUsingStack")

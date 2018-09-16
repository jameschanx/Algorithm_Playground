class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.type = None


class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            node = self.root
            while node:
                if val > node.val:
                    if node.right_child:
                        node = node.right_child
                    else:
                        node.right_child = Node(val)
                        node.right_child.parent = node
                        node.right_child.type = 'right'
                        break
                else:
                    if node.left_child:
                        node = node.left_child
                    else:
                        node.left_child = Node(val)
                        node.left_child.parent = node
                        node.left_child.type = 'left'
                        break
    
    
    def delete(self, val):
        #empty
        if not self.root:
            return
        
        node = self.root
        while node:
            if val > node.val:
                node = node.right_child
            elif val < node.val:
                node = node.left_child
            else:
                break
            
        #no children
        if not node.left_child and not node.right_child:
            if node.type == 'left':
                node.parent.left_child = None
            else:
                node.parent.right_child = None
            return
        
        #two children
        if node.left_child and node.right_child:
            successor = node.right_child
            while successor.left_child:
                successor = successor.left_child
            node.val = successor.val
            #successor has right child
            if successor.right_child:
                successor.right_child.parent = successor.parent
                successor.parent.left_child = successor.right_child
            #successor has no children
            else:
                pass
                successor.parent.left_child = None
            return
            
        #one child
        if node.left_child:
            node.left_child.parent = node.parent
            if node.type == 'left':
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child
        if node.right_child:
            node.right_child.parent = node.parent
            if node.type == 'left':
                node.parent.left_child = node.right_child
            else:
                node.parent.right_child = node.right_child
            
        #not found
        return 

    def _traverse_preorder(self, root):
        if not root:
            return
        print(root.val)
        self._traverse_preorder(root.left_child)
        self._traverse_preorder(root.right_child)
        
    def disp(self):
        node = self.root
        self._traverse_preorder(node)
        print(' ')

    
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(9)
bst.insert(12)
bst.insert(17)
bst.insert(16)
bst.insert(19)
bst.disp()
bst.delete(4)
bst.delete(6)
bst.delete(3)
bst.delete(8)
bst.disp()
bst.delete(15)
bst.disp()
bst.delete(17)
bst.disp()
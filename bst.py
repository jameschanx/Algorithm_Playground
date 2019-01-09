# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 18:13:41 2019

@author: Katy
"""
import numpy as np

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def _insert(self, root, val):
        if not root:
            return TreeNode(val)
        if(val < root.val):
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        return root
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
        
        
    def _delete(self, root, val):
        if not root:
            return None
        elif(val < root.val):
            root.left = self._delete(root.left, val)
        elif(val > root.val):
            root.right = self._delete(root.right, val)
        else:
            #has no children
            if(not root.left and not root.right):
                return None
            #has 2 children
            if(root.left and root.right):
                tmp = self.find_max(root.left)
                root.val = tmp.val
                root.left = self._delete(root.left, root.val)
                return root
            #has 1 children
            if(root.left):
                return root.left
            else:
                return root.right
        return root
    
    def delete(self, val):
        self.root = self._delete(self.root, val)
        
    def find_max(self, root):
        if not root:
            return None
        while root.right:
            root = root.right
        return root
    
    def find_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root
    
    def _print_pre_order(self, root):
        if not root:
            return
        print(root.val)
        self._print_pre_order(root.left)
        self._print_pre_order(root.right)
        
    def print_pre_order(self):
        self._print_pre_order(self.root)
        
    
if __name__=="__main__":
#    bst = BST()
#    bst.insert(6)
#    bst.insert(3)
#    bst.insert(1)
#    bst.insert(4)
#    bst.insert(10)
#    bst.insert(7)
#    bst.insert(8)
#    bst.print_pre_order()
#    print
#    bst.delete(1)
#    bst.print_pre_order()
#    print
#    bst.delete(3)
#    bst.print_pre_order()
#    print
#    bst.delete(10)
#    bst.print_pre_order()
#    print
#    bst.delete(6)
#    bst.print_pre_order()
#    print
#    max_ = bst.find_max()
#    min_ = bst.find_min()
#    print(max_.val)
#    print(min_.val)
#    bst = BST()
#    bst.insert(5)
#    bst.print_pre_order()
#    bst.delete(5)
#    bst.print_pre_order()
    
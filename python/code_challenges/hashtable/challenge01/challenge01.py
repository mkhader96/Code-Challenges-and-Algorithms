class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Solution(root, k):
    '''A function that takes a BST and a value and returns true if there are 2 numbers in the tree that can be summed to equal the value entered'''
    tree_values = []

    def Two_Sum_BST(node):
        if not node:
            return False
        diff = k - node.val
        if diff in tree_values:
            return True
        else:
            tree_values.append(node.val)
        return Two_Sum_BST(node.left) or Two_Sum_BST(node.right)

    return Two_Sum_BST(root)
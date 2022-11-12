class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left
class Tree:  
    def __init__(self):
        self.queue = []
        self.root = None
    
    def convertArrayToBST(self, nums):
        '''The function should return a root node to the newly created binary search tree.'''
        return self.buildBST(nums, 0, len(nums))
        
    def buildBST(self, nums, start, end):
        '''The function should return a root node to the newly created binary search tree.'''
        if start >= end: return None
        return Node(
            value = nums[ (start + end) // 2 ],
            left = self.buildBST(nums, start, (start + end) // 2),
            right = self.buildBST(nums, 1 + ((start+end) // 2), end)
        )
    
    def breadthFirstSearch(self):
        '''The function should return a list of the values in the tree in the order they were encountered.'''
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.value)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree
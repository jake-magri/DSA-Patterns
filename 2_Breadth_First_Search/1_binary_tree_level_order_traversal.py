"""
Problem: Binary Tree Level Order Traversal
Return the level-order traversal of a binary tree (nodes by level).

Approach:
Use a queue for BFS. Process nodes level by level, adding children to the queue.

Time Complexity: O(N) where N is the number of nodes in the tree.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Start with the root node
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Example binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Level Order Traversal:", level_order_traversal(root))

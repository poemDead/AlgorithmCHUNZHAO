"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root: return res

        # 和590同理，但是因为前序，所以先append自己的值
        def preorderTraversal(root,res):
            if root:
                res.append(root.val)
                for child in root.children:
                    preorderTraversal(child, res)
        
        preorderTraversal(root, res)
        return res
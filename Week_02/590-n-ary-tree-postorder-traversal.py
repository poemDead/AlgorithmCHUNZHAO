"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 空树就返回空列表
        res = []
        if not root: return res

        # 如果非空就遍历子节点，进行递归。
        # 后序-->最后把自己的值放入结果
        def posttree(root, res):
            if root:
                for child in root.children:
                    posttree(child, res)
            res.append(root.val)
        
        posttree(root,res)
        return res
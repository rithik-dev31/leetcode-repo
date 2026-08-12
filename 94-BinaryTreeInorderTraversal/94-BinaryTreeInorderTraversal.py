# Last updated: 8/12/2026, 11:32:12 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result=[]

        self.inorder(root,result)

        return result

    def inorder(self,node,result):
        if node is None:
            return

        self.inorder(node.left,result)
        result.append(node.val)
        self.inorder(node.right,result)
        
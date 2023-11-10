# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node:TreeNode,result:List[int]):
            if node:
                # Traverse the left subtree
                dfs(node.left, result)
                # Traverse the right subtree
                dfs(node.right, result)
                # Process the current node
                result.append(node.val)
        result=[]
        dfs(root,result)
        return result        

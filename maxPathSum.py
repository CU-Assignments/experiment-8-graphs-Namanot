class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf') 
        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)  
            right_gain = max(dfs(node.right), 0)
            current_max = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_max)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return self.max_sum
        
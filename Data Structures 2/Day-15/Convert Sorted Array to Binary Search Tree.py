class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        
        def build(nums, left, right):
            if left > right:
                return None
            
            mid = (left + right) / 2
            
            node = TreeNode(nums[mid])
            node.left = build(nums, left, mid-1)
            node.right = build(nums, mid+1, right)
            
            return node
        
        return build(nums, 0, len(nums)-1)

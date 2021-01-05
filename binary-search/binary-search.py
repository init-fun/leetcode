class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid_index = (left+right) // 2     
            mid_ele = nums[mid_index]
            
            if mid_ele == target:
                return mid_index
            elif target > mid_ele:
                left = mid_index + 1
            else:
                right = mid_index - 1
        return -1
            
            
        
        

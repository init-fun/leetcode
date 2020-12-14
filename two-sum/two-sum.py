class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for first_ele in range(len(nums)):
            # first_ele = nums[i]
            sec_ele = first_ele + 1
            while sec_ele < len(nums):
                if (nums[first_ele] + nums[sec_ele]) == target:
                    res.extend([first_ele, sec_ele])
                    return res
                sec_ele += 1
        
            
        

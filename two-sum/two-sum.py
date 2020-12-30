class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use the two pointer technique here
        # set the ptr1 at the 0th index, this pointer will be used to traverse the array
        # initially the second pointer will always be one step ahead of the first pointer
        # check if the sum of the ptr1 + ptr2 is equal to target 
        res = []
        for ptr1 in range(len(nums)):
            ptr2 = ptr1 + 1
            while ptr2 < len(nums):
                if (nums[ptr1] + nums[ptr2]) == target:
                    res.extend([ptr1, ptr2])
                    return res
                ptr2 += 1
        
            
        

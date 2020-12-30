class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # result = [1] * len(nums)
        # for ptr1 in range(len(nums)):
        #     mul_sum = 1
        #     ptr2 = 0
        #     while ptr2 < len(nums):
        #         if ptr1 == ptr2:
        #             ptr2 += 1
        #             continue
        #         mul_sum *= nums[ptr2]     
        #         ptr2 += 1
        #     result[ptr1] = mul_sum
        # return result 
        
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [1] * len(nums)
        
        
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result

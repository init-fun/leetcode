class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # saw the nick white's video and by using the Kdane's algo
        # here we can solve this question
        # so the trick is to compare the current sum to the max_sum that we can by using the prev sum
        
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
​
        return maxSum

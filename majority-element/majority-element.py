class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = -1
        res = None
        for i in set(nums):
            total = nums.count(i)
            if total > max_count:
                max_count = total
                res = i
        return res

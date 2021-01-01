class Solution(object):
    def findDisappearedNumbers(self, nums):
        # res = []
        # for i in range(1,len(nums)+1):
        #     if not i in nums:
        #         res.append(i)
        # return res
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1 
            # get the index of the of the current num in the list
            # make that index's number a negative number ( if it already make it again )
            
            nums[index] = -1 * abs(nums[index])
        res = []
            
            # loop through the new update nums list and 
            # if the num is positive then that num is missing 
        for i in range(len(nums) ):
            if nums[i] > 0:
                res.append(i+1)
        return res
​

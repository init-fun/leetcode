class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 2:
                continue
            else:
                return num
        return False
                

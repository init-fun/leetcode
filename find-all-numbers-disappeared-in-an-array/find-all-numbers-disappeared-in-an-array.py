class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if not i in x:
                res.append(i)
        return res

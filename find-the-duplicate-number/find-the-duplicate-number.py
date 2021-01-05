class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        return max(d, key = d.get)

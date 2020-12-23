class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = s.split()
        if tmp:
            return len(tmp[-1])
        return 0
        

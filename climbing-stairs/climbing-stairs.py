class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 :
            return 1
        if n==2:
            return 2
        p1 = 1
        p2 = 2
        
        for i in range(3,n+1):
            p3 = p2+p1
            p1 = p2
            p2 = p3
        return p2

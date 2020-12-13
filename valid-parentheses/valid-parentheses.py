class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = list(s)
        stack = []
        open_brac = ['(','{','[']
        clos_brac = [')','}',']']
        index = 0
        total_len = len(lst)
        if lst[index] in clos_brac:
            return False
        else:
            while index < total_len:
                if lst[index] in open_brac:
                    # pos = open_brac.index(lst[index])
                    stack.append(lst[index])
                elif lst[index] in clos_brac:
                    stack_pos = clos_brac.index(lst[index])
                    ele_to_remove = open_brac[stack_pos]
​
                    if stack and ele_to_remove == stack[-1]:    
                        stack.pop()
                    else:
                        stack.append(lst[index])
                index += 1
        if stack:
            return False
        return True

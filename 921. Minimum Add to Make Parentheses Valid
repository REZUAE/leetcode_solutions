class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        L_count = 2
        R_count = -2
        "()))(("
              ^
        """

        L_count = 0
        R_count = 0 
        for char in s:
            if char == '(':
                L_count += 1
            else:
                if L_count > 0 :
                    L_count -=1
                else:
                    R_count +=1

        return abs(L_count)+abs(R_count)
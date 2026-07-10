class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=sorted(s)
        tt=sorted(t)
        if tt==ss : 
            return True
        else :
            return False
        
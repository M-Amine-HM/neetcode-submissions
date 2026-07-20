class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        maxSub=0
        d={}
        for c in range(len(s)):
            print(s[c])
            if s[c] not in d:
                cc=s[c]
                d[cc]=c
                if maxSub<c-i+1:
                    maxSub=c-i+1
            else:
                if maxSub<c-i:
                    maxSub=c-i
                new=d[s[c]]+1
                if new>i :
                    i=d[s[c]]+1
                
                print(i)
                d[s[c]]=c
            print(d)
        return maxSub







































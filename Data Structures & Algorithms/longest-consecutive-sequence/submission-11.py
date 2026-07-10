class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[] :
            return 0
        maxc=1
        c=1
        s = sorted(set(nums))
        s=list(s)
        print(s)
        for i in range(1,len(s)) :
            if s[i]-s[i-1]==1 :
                c+=1
                print(c)
            else :
                if maxc<c:
                    maxc=c
                c=1
        if maxc<c:
            maxc=c
        return maxc
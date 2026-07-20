class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSub=0
        #ss=set()
        j=0
        l=[]
        l.append(set())
        index=0
        for i in s : 
            if i not in l[j] :
                l[j].add(i)
                if len(l[j])>maxSub:
                    maxSub=len(l[j])
            else :
                if len(l[j])>maxSub : 
                    maxSub=len(l[j])
                j+=1
                l.append(set())
        return maxSub
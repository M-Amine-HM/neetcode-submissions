class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=sorted(nums)
        left=0
        right=len(s)-1
        middle=0
        result=set()
        while left<right : 
            r=s[left]+s[right]
            new=s[left+1:right]
            if -r in new :
                t=(-r,s[left],s[right])
                if t not in result :
                    result.add(t) 
            if -r>0 :
                left+=1
            else :
                right-=1
        rr=[]
        for i in result :
            rr.append(list(i))
        return rr
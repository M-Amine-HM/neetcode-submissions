class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd=1
        for i in nums :
            prd=prd*i
        result=[1]*len(nums)
        for i in range(len(nums)):
            if prd==0  :
                if nums[i]!=0:
                    result[i]=0
                else :
                    new=nums[:]
                    new[i]=1
                    prd1=1
                    for j in new :
                        prd1=prd1*j
                    result[i]=prd1
            else :
                result[i]=prd//nums[i]
        return result
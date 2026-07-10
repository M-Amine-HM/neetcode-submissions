class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        result=[1]*len(nums)
        for i in range(len(nums)):
            if i==0 :
                prefix[i]=nums[i]
            else :
                prefix[i]=prefix[i-1]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1 :
                suffix[i]=nums[i]
            else :
                suffix[i]=suffix[i+1]*nums[i]
        for i in range(len(result)) :
            if i!=0 and i!=len(nums)-1:
                result[i]=prefix[i-1]*suffix[i+1]
            elif i==0 :
                result[i]=suffix[i+1]
            else :
                result[i]=prefix[i-1]
        return result
        # prd=1
        # for i in nums :
        #     prd=prd*i
        # result=[1]*len(nums)
        # for i in range(len(nums)):
        #     if prd==0  :
        #         if nums[i]!=0:
        #             result[i]=0
        #         else :
        #             new=nums[:]
        #             new[i]=1
        #             prd1=1
        #             for j in new :
        #                 prd1=prd1*j
        #             result[i]=prd1
        #     else :
        #         result[i]=prd//nums[i]
        # return result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=set()
        for i in range(len(nums)-1) : 
            s=set()
            for j in  range(i+1 ,len(nums)) :
                t=nums[i]+nums[j]
                if -t not in s :
                    s.add(nums[j])
                else :
                    r=(nums[i],nums[j],-t)
                    if r not in result :
                        result.add(r)
        sol=[]
        for j in result :
            sol.append(list(j)) 
        return sol
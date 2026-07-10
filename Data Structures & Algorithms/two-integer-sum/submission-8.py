class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r=[]
        freq={}
        for i in range(len(nums)) :
            s=target-nums[i]
            if s in freq :
                return sorted([i,freq[s]])
            else :
                freq[nums[i]]=i

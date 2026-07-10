class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r=[]
        freq={}
        for i in range(len(nums)) :
            s=target-nums[i]
            if s in freq :
                return [freq[s],i]
            else :
                freq[nums[i]]=i

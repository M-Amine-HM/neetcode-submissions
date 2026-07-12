class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxW=0
        w=0
        while(left<right) :
            w=abs(left-right)*min((heights[left],heights[right]))
            if maxW<w : 
                maxW=w
            if heights[left]<heights[right] :
                left+=1
            else : 
                right-=1
        return maxW
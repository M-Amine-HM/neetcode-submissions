class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq={}
        if len(nums)==1 :
            return nums
        for i in (nums):
            if i in frq :
                frq[i]+=1
            else :
                frq[i]=1
        l=[-1000]*len(nums)
        for key , value in frq.items() :
            if l[value-1]!=-1000:
                l[value-1].append(key)
            else :
                l[value-1]=[key]
        r=[]
        print(frq)
        print(l)
        for i in range(len(l)-1,-1,-1) :
            if l[i]!=-1000 :
                if isinstance(l[i], list):
                    for t in l[i] :
                        r.append(t)
                        k-=1
                        print(r)
                else :
                    r.append(l[i])
                    k-=1
            if k==0 : 
                break
        return r 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frq={}
        for i in strs :
            st=sorted(i)
            ch=""
            #print(st)
            for k in st :
                ch=ch+k
            if ch not in frq :
                frq[ch]=[]
                frq[ch].append(i)
                #print(frq)
            else :
                frq[ch].append(i)
        lst=[]
        for index,(key,value) in enumerate(frq.items()) :
            lst.append(value)
        
        return lst
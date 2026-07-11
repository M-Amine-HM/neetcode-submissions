class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz"
        num="0123456789"
        s=s.lower()
        newS=[]
        for i in s :
            if i in alp or i in num  :
                newS.append(i)
        print(newS)
        m=newS[-1::-1]
        print(m)
        if m==newS :return(True) 
        else : return(False)
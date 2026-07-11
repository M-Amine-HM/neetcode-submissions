class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz"
        upalp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num="0123456789"
        newS=""
        for i in s :
            if i in upalp  :
                newS=newS+i.lower()
            elif i in alp or i in num :
                newS=newS+i
        print(newS)
        m=newS[-1::-1]
        print(m)
        if m==newS :return(True) 
        else : return(False)
class Solution:
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]

            res.append(word)

            i = j + 1 + length

        return res
    # def encode(self, strs: List[str]) -> str:
    #     if strs==[]: 
    #         return "00"
    #     if strs==[""] :
    #         return "11"
    #     ch=""
    #     for i in strs :
    #         ch=ch+i+" "
    #     ch=ch[:len(ch)-1]
    #     return ch

    # def decode(self, s: str) -> List[str]:
    #     if s=="11" :
    #         return [""]
    #     if s=="00" :
    #         return []
    #     l=[]
    #     ch=""
    #     for i in s :
    #         if i==" ":
    #             l.append(ch)
    #             ch=""
    #         else :
    #             ch=ch+i
    #     l.append(ch)
    #     return l
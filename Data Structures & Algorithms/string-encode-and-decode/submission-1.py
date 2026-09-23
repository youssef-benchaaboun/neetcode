class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            code=str(len(s)) +"#"
            result += code + s
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while(i < len(s)):
            str_len=0
            while(s[i]!="#"):
                str_len=str_len*10 + int(s[i])
                i+=1
            i+=1
            strs=""
            while(str_len):
                strs +=s[i]
                str_len -=1
                i +=1
            result.append(strs)
        return result

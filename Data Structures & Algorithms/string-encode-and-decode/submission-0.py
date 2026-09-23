class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            code=str(len(s)) +"#"
            result += code + s
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        new=True
        i=0
        while(i < len(s)):
            if new:
                str_len=0
                while(s[i]!="#"):
                    str_len=str_len*10 + int(s[i])
                    i+=1
                i+=1
                new=False
            strs=""
            while(str_len):
                strs +=s[i]
                str_len -=1
                i +=1
            result.append(strs)
            new=True
        return result

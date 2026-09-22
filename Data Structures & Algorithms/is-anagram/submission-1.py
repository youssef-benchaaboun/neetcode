class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list:list=[]
        t_list:list=[]
        for i in range(256):
            s_list.append(0)
            t_list.append(0)
        for c in s:
            s_list[ord(c)]+=1
        for c in t:
            t_list[ord(c)]+=1
        return  s_list==t_list
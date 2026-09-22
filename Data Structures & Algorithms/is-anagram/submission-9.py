class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        for c in s:
            s_dic[c] = 1 + s_dic.get(c,0) #get safer to get value and default if not  excist
        for c in t:
            t_dic[c] = 1 + t_dic.get(c,0)
        for c in s_dic:
            if s_dic[c] != t_dic.get(c,0):
                return False
        return len(s)==len(t)
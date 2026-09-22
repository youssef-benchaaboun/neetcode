class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        for c in s:
            if c in s_dic:
                s_dic[c] += 1
            else:
                s_dic[c] = 0
        for c in t:
            if c in t_dic:
                t_dic[c] += 1
            else:
                t_dic[c] = 0
        return s_dic == t_dic
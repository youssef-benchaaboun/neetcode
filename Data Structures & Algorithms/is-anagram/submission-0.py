class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 256
        t_list = [0] * 256
        for c in s:
            s_list[ord(c)] += 1
        for c in t:
            t_list[ord(c)] += 1
        return s_list == t_list
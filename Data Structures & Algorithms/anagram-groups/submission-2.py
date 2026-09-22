class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_string={}

        for s in strs:
            s_key=[0]*26
            for c in s:
                s_key[ord(c)-ord("a")]+=1
            s_key = tuple(s_key)
            if s_key in hash_string:
                hash_string[s_key].append(s)
            else:
                hash_string[s_key]=[s]
        return list(hash_string.values())
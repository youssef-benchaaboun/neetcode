class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_string={}

        for s in strs:
            s_dic:dict={}
            for c in s:
                s_dic[c] =1+s_dic.get(c,0)
            string=""
            for c in range(ord("a"),ord("z")+1):
                if chr(c) in s_dic:
                    string += chr(c) + str(s_dic[chr(c)])
            if string in hash_string:
                hash_string[string].append(s)
            else:
                hash_string[string]=[s]
        return list(hash_string.values())
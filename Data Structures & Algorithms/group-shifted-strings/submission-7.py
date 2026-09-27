class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        gdict=defaultdict(list)
        for s in strings:
            key=[]

            for i in range(len(s)-1):
                val = (ord(s[i + 1]) - ord(s[i])) % 26
                key.append(val)
            
            key_t=tuple(key)
            gdict[key_t].append(s)
        
        return list(gdict.values())
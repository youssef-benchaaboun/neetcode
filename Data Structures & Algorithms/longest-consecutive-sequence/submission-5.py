class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict=defaultdict(int)
        for nb in nums:
                my_dict[nb]=1
        for nb in list(my_dict):
            if nb not in my_dict:
                 continue
            i=1
            while (nb + i) in my_dict:
                my_dict[nb] += my_dict[nb+i]
                my_dict.pop(nb + i)
                i+=1
        
        maxlen=0
        for key in my_dict:
            if maxlen < my_dict[key]:
                maxlen = my_dict[key]
        return maxlen
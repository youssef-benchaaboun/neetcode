class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict=defaultdict(list)
        for nb in nums:
                my_dict[nb]=[nb]
        for nb in list(my_dict):
            i=1
            while (nb + i) in my_dict:
                my_dict[nb].extend(my_dict[nb+i])
                my_dict.pop(nb + i)
                i+=1
        
        maxlen=0
        for key in my_dict:
            if maxlen < len(my_dict[key]):
                maxlen = len(my_dict[key])
        return maxlen
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping={}
        for i in range(len(nums2)):
            mapping[nums2[i]]=i
            i+=1
        result=[]
        for nb in nums1:
            result.append(mapping[nb])
        return result

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for n in range(len(nums)+1):
            count=0
            for nb in nums:
                if nb>=n:
                    count +=1
            if count==n:
                return count
        return -1
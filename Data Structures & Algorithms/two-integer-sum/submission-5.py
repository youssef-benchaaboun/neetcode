class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab_hash={}
        for i ,value in enumerate(nums):
            diff=target-value
            if (diff) in tab_hash:
                return [tab_hash[diff],i] 
            if value not in tab_hash:
                tab_hash[value] =i
        return []
# Search for the complement while building the hash map.
# This replaces "build everything -> search everything" with one incremental pass.
# Store only what is needed from previously seen values.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab_hash={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if (diff) in tab_hash:
                return [tab_hash[diff],i] # for duplicate number check if exsit before adding to hash avoid unssecairy hash element also for dup elemnt
            if nums[i] not in tab_hash:
                tab_hash[nums[i]] =i
        return []
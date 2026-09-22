class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab_hash={}
        for i in range(len(nums)):
            if nums[i] not in tab_hash:
                tab_hash[nums[i]] =[i]
            else:
                tab_hash[nums[i]].append(i)
        for i in range(len(nums)):
            if (target - nums[i]) in tab_hash:
                for j in tab_hash[target-nums[i]]:
                    if i !=j:
                        return [i,j]
        return [-1,-1]
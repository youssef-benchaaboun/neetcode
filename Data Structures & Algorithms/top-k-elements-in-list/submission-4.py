class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_hash=defaultdict(int)
        for nb in nums:
            frequency_hash[nb] += 1

        sorted_frequency=defaultdict(list)
        max_freque=0
        for key in frequency_hash:
            if max_freque<frequency_hash[key]:
                max_freque=frequency_hash[key]
            new_key=frequency_hash[key]
            new_value=key
            sorted_frequency[new_key].append(new_value)
        
        solution=[]
        while(len(solution)<k and max_freque >0):
            for nb in sorted_frequency.get(max_freque,[]):
                solution.append(nb)
                if len(solution)==k:
                    break
            max_freque -=1
        return solution

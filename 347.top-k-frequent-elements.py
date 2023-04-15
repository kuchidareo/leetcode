from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_array = Counter(nums)
        
        return heapq.nlargest(k, freq_array.keys(), key=freq_array.get)

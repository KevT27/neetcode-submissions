from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1

        highest_keys = sorted(dic, reverse=True, key=dic.get)[:k]

        return highest_keys
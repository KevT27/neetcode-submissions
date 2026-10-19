class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Create Dictionary
        # Iterate through nums
        # Check if Value already exists
        # Add value to dict, otherwise return true

        dic = {}

        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1

        return False

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        max_ = len(nums)
        k = 0
        i = 0

        for num in nums[:]:

            if num == val:
                # Remove Num from nums
                del nums[i]
                i -= 1
            else:
                k += 1  
                
            i += 1

        return k
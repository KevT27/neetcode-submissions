class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        max_ = len(nums)
        k = 0
        i = 0

        for num in nums[:]:
            print(f"Current Iteration: {i}")

            print(f"Current Num: {num}")
            print(f"Current List: {nums}")

            if num == val:
                print(f"{num} = {val}")
                # Remove Num from nums
                print(f"Deleting: {nums[i]}")
                del nums[i]
                i -= 1

            else:
                print(f"{num} != {val}")
                k += 1  
            
            i += 1

        print(nums)
        return k
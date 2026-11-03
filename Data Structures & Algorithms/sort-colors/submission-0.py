class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) > 1:
            left = nums[:len(nums)//2]
            right = nums[len(nums)//2:]

            self.sortColors(left)
            self.sortColors(right)

            i = j = k = 0
            while (i < len(left) and j < len(right)):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    k+=1
                    i+=1
                else:
                    nums[k] = right[j]
                    k+=1
                    j+=1
            nums[k:] = left[i:] + right[j:]
        return nums
        
        
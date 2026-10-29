class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            left = nums[:len(nums)//2]
            right = nums[len(nums)//2:]

            self.sortArray(left)
            self.sortArray(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            nums[k:] = left[i:] + right[j:]
        return nums
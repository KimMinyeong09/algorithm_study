class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # basis : len == 0, 1, 2 -> 0
        n = len(nums)
        if (n < 3): return 0

        prev_diff = nums[0] - nums[1]
        num_subarrays = 0
        count = 0

        for i in range(1, n-1):
            cur_diff = nums[i] - nums[i+1]
            
            if prev_diff == cur_diff:
                count += 1
                num_subarrays += count
            else:
                count = 0
                prev_diff = cur_diff
            
        return num_subarrays

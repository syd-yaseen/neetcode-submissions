class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if (num-1) not in num_set:  
                streak = 0
                curr = num
                while curr in num_set:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res
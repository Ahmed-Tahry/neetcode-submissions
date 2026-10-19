class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bingo = {}
        for i in range(0, len(nums)):
            bingo[nums[i]] = i
            
        # FIX: Changed nums[i] to len(nums)
        for i in range(0, len(nums)):
            if (target - nums[i]) in bingo and i != bingo[target - nums[i]]:
                return [i, bingo[target - nums[i]]]
        return []

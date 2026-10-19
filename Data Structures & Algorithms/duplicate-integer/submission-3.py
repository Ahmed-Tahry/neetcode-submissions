class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsetto = set(nums)
        if len(nums)> len(hashsetto):
            return True
        else :
            return False

        
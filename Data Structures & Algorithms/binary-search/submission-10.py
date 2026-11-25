class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums) -1
        if nums[i] == target :
            return i
        if nums[j] == target :
            return j
        def searching(nums,target,i,j):

            if i > j :
                return -1
            m = (i+j) // 2
            if target == nums[m] :
                return m

            if target < nums[m] :
                return searching(nums,target,i,m-1)
            if target > nums[m] :
                return searching(nums,target,m+1,j)
        
        return searching(nums,target,i,j)
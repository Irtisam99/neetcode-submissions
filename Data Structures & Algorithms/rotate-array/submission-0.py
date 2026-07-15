class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=[0]*len(nums)
        for n in range(len(nums)):
            new[(n+k)%(len(nums))]=nums[n]

        nums[:]=new

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        n=len(nums)

        for i in range(n):
            count=0
            for j in range(i,n):
                if nums[j]==0:
                    break;
                count=count+1
            res=max(res,count)
        return res
        
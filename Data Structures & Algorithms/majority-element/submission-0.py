class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        for key,value in count.items():
            if value>n//2:
                return key

        






        
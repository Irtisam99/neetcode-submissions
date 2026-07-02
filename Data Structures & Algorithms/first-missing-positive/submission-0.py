class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing=1
        while True:
            flag=True
            for num in nums:
                if num==missing:
                    flag=False
                    break

            if flag==True:
                return missing
            missing+=1
        
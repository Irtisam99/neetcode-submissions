class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for c in nums:
            count[c]=1+count.get(c,0)
        
        arr=[]
        for ind,val in count.items():
            arr.append([val,ind])
        arr.sort()

        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
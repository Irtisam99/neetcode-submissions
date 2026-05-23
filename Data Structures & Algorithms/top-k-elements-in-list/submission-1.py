class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Min-Heap
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        heap=[]
        for key in count.keys():
            heapq.heappush(heap,(count[key],key))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while len(res)<k:
            res.append(heapq.heappop(heap)[1])
        return res


        
        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for i in strs:
            sortedS="".join(sorted(i))
            result[sortedS].append(i)
            
        return list(result.values())
            
            
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=[]
        i=j=0
        
        while i<len(word1) and j<len(word2):
            string.append(word1[i])
            i+=1
            string.append(word2[j])
            j+=1

        string.append(word1[i:])
        string.append(word2[j:])

        return "".join(string)
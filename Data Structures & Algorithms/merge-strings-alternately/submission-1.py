class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        m=len(word1)
        n=len(word2)
        string=[]

        while i<m or j<n:
            if i<m:
                string.append(word1[i])
            i+=1
            if j<n:
                string.append(word2[j])
            j+=1
        return "".join(string)

        
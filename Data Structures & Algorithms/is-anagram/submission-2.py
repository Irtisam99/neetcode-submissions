class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq=collections.defaultdict(int)
        t_freq=collections.defaultdict(int)

        for i in s:
            s_freq[i]+=1
        for i in t:
            t_freq[i]+=1

        if s_freq == t_freq:
            return True
        else:
            return False

        
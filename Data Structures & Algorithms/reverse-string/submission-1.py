class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointers
        r=0
        l=len(s)-1

        while r<l:
            s[r],s[l]=s[l],s[r]
            r+=1
            l-=1
        
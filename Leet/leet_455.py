class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        i = len(g)-1
        j = len(s)-1
        while i >=0 and j >=0:
            if g[i] <= s[j]:
                count+=1
                i-=1
                j-=1
            else:
                i-=1
        # for i in range (len(g)):
        #     if g[i] in s:
        #         s.remove(g[i])
        #         count+=1
        return count
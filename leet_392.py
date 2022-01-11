def isSubsequence(s, t):
        s= list(s)
        count=0
        for ch in s:
            if ch in t:
                a=t.find(ch)
                t=t[a+1:]
                count+=1
        if count == len(s): return True
        else: return False
s = "acb"
t = "ahbgdc"
print(isSubsequence(s,t))
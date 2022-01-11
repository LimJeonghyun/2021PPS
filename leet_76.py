#미완성
def minWindow(s, t):
    count = len(t)
    listing=[]
    # counts=0
    if len(s) < len(t): return'""'
    while 1:
        for i in range(len(s)):
            listing.append(s[i:i+count])
        print(listing)
        l = len(listing)
        for i in range(len(t)):
            # print(t[i])
            j=0
            while 1:
                if not t[i] in listing[j]:
                    del listing[j]
                    l-=1
                    # print(l, j)
                else: j+=1
                if j == l or j < 0:break
            print(listing) 
        if len(listing) == 0 : count+=1
        else: break
                  
    return "".join(listing)
                



# from collections import Counter

# def minWindow(s, t):
        # count, remain = Counter(t), len(t) #count = {A:1, B:1, C:1}, remain = len(t) (3)
        # i, left, right = 0, -1, -1
        # for j, c in enumerate(s):  # enumerate: tuple 형태로 변환 (0, A) => j: index 번호, c: 원소
        #     remain -= count[c] > 0 # ex) 3-count(A) => 3-1 > 0
        #     count[c] -= 1 # ex) count(A) -= 1 = 0
        #     if remain:  # ex) remain > 0 continue
        #         continue
        #     while count[s[i]] < 0:  # greedily discard uneeds count[s[0]] => count(A) < 0 => count(A)+=1 i+=1
        #         count[s[i]] += 1
        #         i += 1
        #     if right == -1 or j-i+1 < right-left+1:
        #         left, right = i, j
        # return s[left:right+1]

# def minWindow(s, t):
#     if len(s) < len(t):
#         return '""'
#     else:
#         # s=list(s)
#         # t=list(t)
#         a=0
#         for i in range(len(t)):
#             while 1:
#                 a = s.find(t[i], s.find(t[i], a))
#                 if a == len(s)-1 or a==-1:break
#                 print(a)
#                 a+=1
#                 for j in range(i+1,len(t)):
#                     if a-1 == -1 or a+1 == len(s): break
#                     else:
#                         if s[a-1] == t[i]:
                            


s="bbaa"
t="aba"
print(minWindow(s, t))
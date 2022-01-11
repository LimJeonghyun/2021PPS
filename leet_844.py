# #미완성 

# def backspaceCompare(s, t):
#     # s, t = list(s), list(t)
#     a, b = 0, 0
#     lists, listt = [],[]
    
#     while 1:
#         a = s.find("#", s.find("#", a+1))
#         print(a)
#         if a == -1 or a+1 == len(s): break
#         lists.append(a)
#     # while 1:
#     #     b = t.index("#", s.index("#", b))
#     #     print(b)
#     #     listt.append(b)
#     #     if b == -1 : break
    
#     sl = list(s)
#     print(sl)
#     for i in sl:
#         sl.remove("#")
#     for i in lists:
#         del sl[i-1]

#     return sl




# s = "ab##"
# t = "ad#c"    
# print(backspaceCompare(s, t))

def backspaceCompare(self, s, t):
        def make(n):
            r = []
            for c in n:
                if c != '#':
                    r.append(c)
                else:
                    if r:
                        r.pop(-1)
            return ''.join(r)
        return make(s) == make(t)
def repeatedStringMatch(self, A, B):
        A_len = len(A)
        B_len = len(B)
        
        answer = B_len // A_len + 2
        temp = A * answer
        if B not in temp:
            return -1
        while B in A * (answer-1):
            answer = answer - 1
        return answer

# def repeatedStringMatch(a, b):
#     if b.count(a) == 0: return -1
#     else:
#         return b.count(a)

# a = "abcd"
# b = "cdabcdab"
# print(repeatedStringMatch(a,b))
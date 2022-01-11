def convert(self, s: str, numRows: int) -> str:
        step = 0 if numRows == 1 else -1
        res = [''] * numRows
        i = 0
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1: step = -step # change direction
            
            i += step
        return ''.join(res)

# def convert(s, numRows):
#     count = 0
#     lists = []
#     wording = ""
#     for i in range (len(s)):
#         if count!=0 and count%numRows == 0:
#             lists.append(list(wording))
#             wording=""
#             count = 0
#             lists.append(list(s[i]))
#             if numRows%2 == 0:
#                 lists.append(list(s[i-1]))
#         else:
#             wording += s[i]
#             count+=1
#             if (i+1) == len(s):
#                 lists.append(list(wording))
#     print(lists)
#     # word = " "
#     # for i in range (len(lists)):
#     #     word=word+lists[i]
#     # return word
#         # print(wording)
#         # print(lists)
                
# s = "PAYPALISHIRING"
# numRows = 3
# print(convert(s, numRows))
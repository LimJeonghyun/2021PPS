def countAndSay(n):
    listing=["1"]
    # if n == 1: 
    #     listing = [1]
    if n != 1:
        order=""
        for i in range(1,n):
            listings=list(set(listing))
            for j in range(len(listings)):
                a=listing.count(listings[j])
                order+=str(a)
                order+=str(listings[j])
            listing=[]
            listing=list(order)
            order=""
        # print(listing)
        # answer = ""
        # for i in range (len(listing)):
        #     answer+=listing[i]

    return "".join(listing)


      

n=4
print(countAndSay(n))

# res = '1'
# for _ in range(1, n):
#     prev, count = '.', 0
#     curr_str = ""
#     for char in res:
#         if char == prev or prev == '.':
#             count += 1
#         else:
#             curr_str += str(count) + prev
#             count = 1
#             prev = char
#         curr_str += str(count) + prev
#         res = curr_str
# return res
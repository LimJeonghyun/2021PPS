num = int(input())
from collections import deque

cards = deque(range(1, num+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

#시간 초과
# card = int(input())
# cardl=[x for x in range(card)]
# cardl=[]
# answer=0

# for i in range(1,card,2):
#     cardl.append(i+1)
# print(cardl)
# if card %2 == 0:
#     answer = cardl[len(cardl)-1]
# else:
#     answer=cardl[len(card)-2]
    
# print(answer)
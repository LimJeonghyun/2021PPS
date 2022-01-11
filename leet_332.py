def findItinerary(tickets):
    st = []
    answer = []
    for element in tickets:
        answer += element
    answer = list(sorted(set(answer)))
    return answer

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))
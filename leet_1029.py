def twoCitySchedCost(costs):
        count_minors = []
        l, result = len(costs), 0
        
        for each in costs:
            count_minors.append([each[0], each[0] - each[1]])
        
        count_minors = sorted(count_minors, key=lambda x: x[1])
        
        for i in range(int(l/2)):
            result += count_minors[i][0]
        for j in range(int(l/2), l):
            result += count_minors[j][0] - count_minors[j][1]
        
        return result
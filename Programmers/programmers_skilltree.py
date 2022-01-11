def solution(skill, skill_trees):
    answer = 0
    
    for i in range (len(skill_trees)):
        case = 0
        check = 0
        for ch in skill_trees[i]:
            if ch in skill:
                check+=1
            if ch == skill[case]:
                case +=1
                if case == len(skill):
                    break
            
        if case == check:
            answer+=1
    return answer

# skill = input("")
# skill_trees=input("")
# skill_trees = skill_trees.split()

# skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "AAAAVCFEFED"]
# print(solution(skill, skill_trees))
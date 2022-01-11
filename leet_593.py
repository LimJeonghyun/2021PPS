# from typing_extensions import NotRequired


def validSquare(p1, p2, p3, p4):
    points=[p1, p2, p3, p4]
    # points.sort(key=lambda x:x[0])
    vale = []
    for i in range(len(points)):
        result=0
        for j in range(1+i, len(points)):
            result = ((points[j][0]-points[i][0])**2+(points[j][1]-points[i][1])**2)
            vale.append(result)
    vale.sort()
    if vale[0] == vale[1] == vale[2] == vale[3] !=0 and vale[4]==vale[5]: return True
    else: return False
    # a = vale.count(vale[0])
    # if a== 4: return True 
    # else: return False
p1 = [1,0]
p2 = [-1,0]
p3 = [0,1]
p4 = [0,-1]
print(validSquare(p1, p2, p3, p4))
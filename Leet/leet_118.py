def generate(numRows):
        pascal = []
        pascal.append([1])
        
        for i in range (1, numRows):
            if i == 1:
                pascal.insert(1,[1,1])
            else :
                per = []
                for j in range(i+1):
                    if j-1 == -1 or j+1 == i+1:
                        per.insert(j, 1)
                    else:
                        per.insert(j, pascal[i-1][j]+pascal[i-1][j-1])
                print("*",per)
                pascal.insert(i, per)
        return pascal

print(generate(5))
testcase = int(input(""))

result = [] 

for i in range (testcase):
    t = 0
    count=0
    student = input("")
    case = student.split()
    
    for x in range (1,int(case[0])+1):
        t = t+int(case[x])
    avg = t/int(case[0])
    
    for x in range (1,int(case[0])+1):
        if int(case[x]) > avg:
            count=count+1
    result.append(count/int(case[0])*100)


for i in range (testcase):
    print("%.3f"%result[i]+"%")
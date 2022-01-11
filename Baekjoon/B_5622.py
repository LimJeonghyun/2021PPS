number = input("")

n1 = ['A', 'B', 'C']
n2 = ['D', 'E', 'F']
n3 = ['G', 'H', 'I']
n4 = ['J', 'K', 'L']
n5 = ['M', 'N', 'O']
n6 = ['P', 'Q', 'R', 'S']
n7 = ['T', 'U', 'V']
n8 = ['W', 'X', 'Y', 'Z']

total = 0
x=0

for i in range (len(number)):
    tim = 2
    if number[i] in n1:
        x=1
    elif number[i] in n2:
        x=2
    elif number[i] in n3:
        x=3
    elif number[i] in n4:
        x=4
    elif number[i] in n5:
        x=5
    elif number[i] in n6:
        x=6
    elif number[i] in n7:
        x=7
    elif number[i] in n8:
        x=8
    total = total+tim+1*x
print(total)
def fizzBuzz(n):
    answer = []
    for i in range(n):
        if (i+1)%3==0 and (i+1)%5 ==0:
            result="FizzBuzz"
        elif (i+1)%3==0:
            result = "Fizz"
        elif (i+1)%5==0:
            result = "Buzz"
        else:
            result = str(i+1)
        answer.append(result)
    return answer

print(fizzBuzz(15))
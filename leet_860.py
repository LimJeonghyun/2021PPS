def lemonadeChange(bills):
    money = 0
    case = 0
    count=0
    for each in bills:
        print("*",money)
        change = 0
        change = each-5
        print("-", change)
        if money-change >=0: 
            money=money-change
            case = 1
        elif money-change < 0:
            return False
            break
        print("&", money)
        money=money+each
        print(money)
    if case == 1: return True

bills = [5,5,10,10,20]
# bills = [5,10,5,20,5,10,5,20,5,10,5,20,5,10,5,20,5,10]
print(lemonadeChange(bills))

# def lemonadeChange(self, bills):
#         my_money = {5: 0, 10: 0, 20: 0}
        
#         for each in bills:
#             my_money[each] += 1
#             # 
#             charge = each - 5
#             if charge != 0:
#                 if charge == 5:
#                     if my_money[charge] != 0:
#                         my_money[charge] -= 1
#                     else:
#                         return False
#                 if charge == 15:
#                     if my_money[10] >= 1 and my_money[5] >= 1:
#                         my_money[10] -= 1
#                         my_money[5] -= 1
#                     elif my_money[5] >= 3:
#                         my_money[5] -= 3
#                     else:
#                         return False
            
#         return True
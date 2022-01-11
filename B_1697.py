lo = input().split()
plo, tlo  = int(lo[0]), int(lo[1])
if plo > tlo : dif = plo - tlo
else: dif = tlo-plo
count = dif/plo
print(count)
dif = dif%plo
print(dif)
count +=dif

print(int(count))
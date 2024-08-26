import random

list100 = []
for i in range(100):
    list100.append(random.randint(1, 50))

if list100[0] > list100[1]:
    max1 = list100[0]
    max2 = list100[1]
else:
    max1 = list100[1]
    max2 = list100[0]

for i in range(2, 100):
    if list100[i] >= max1:
        max2 = max1
        max1 = list100[i]
    elif list100[i] > max2:
        max2 = list100[i]

print("Первое максимальное ", max1)
print("Второе максимальное ", max2)


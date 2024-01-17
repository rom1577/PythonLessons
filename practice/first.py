s1 = input("Строка 1: ")
s2 = input("Строка 2: ")
s3 = []

for i in range(len(s1)):
    s3.append(s1[i])
for i in range(len(s2)):
    s3.append(s2[i])

print("".join(s3))
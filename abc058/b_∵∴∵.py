O = input()
E = input()

password = ''

for i in range(len(O) + len(E)):
    if i % 2 == 0:
        password += O[i // 2]
    else:
        password += E[i // 2]

print(password)
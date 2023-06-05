X = int(input())

deposit = 100
year = 0

while deposit < X:
    deposit += deposit // 100
    year += 1

print(year)
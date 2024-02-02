N = int(input())

bin_N = bin(N)
reversed_N = reversed(list(str(bin_N)))

ctz = 0

for i in reversed_N:
    if i == '1':
        break
    else:
        ctz += 1

print(ctz)
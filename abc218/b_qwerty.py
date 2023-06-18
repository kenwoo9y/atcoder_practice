P = list(map(int, input().split()))

S = ''

for i in range(len(P)):
    S += chr(P[i] + 96)

print(S)
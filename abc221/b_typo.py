S = list(input())
T = list(input())

result = False

if S == T:
    result = True

for i in range(len(S) - 1):
    S[i], S[i + 1] = S[i + 1], S[i]
    if S == T:
        result = True
        break
    S[i], S[i + 1] = S[i + 1], S[i]

print('Yes' if result else 'No')
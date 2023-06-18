S = input()

counter = 0

for i in range(len(S) // 2):
    if S[i] != S[-1 - i]:
        counter += 1

print(counter)
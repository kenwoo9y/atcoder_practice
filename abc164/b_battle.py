A, B, C, D = map(int, input().split())

win = False

while A > 0:
    C -= B
    if C <= 0:
        win = True
        break
    A -= D

print('Yes' if win else 'No')
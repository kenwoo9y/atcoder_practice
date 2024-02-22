def length(x1, x2):
    if abs(x1 - x2) == 1 or abs(x1 - x2) == 4:
        return "short"
    else:
        return "long"

S = list(input())
T = list(input())
S1, S2 = S[0], S[1]
T1, T2 = T[0], T[1]

values = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5
}

if length(values[S1], values[S2]) == length(values[T1], values[T2]):
    print("Yes")
else:
    print("No")
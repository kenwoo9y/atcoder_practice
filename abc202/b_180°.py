S = input()

list_S = list(S[::-1])

for i in range(len(S)):
    if list_S[i] == "6":
        list_S[i] = "9"
    elif list_S[i] == "9":
        list_S[i] = "6"

result = "".join(list_S)

print(result)
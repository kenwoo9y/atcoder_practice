N = int(input())
S = input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = S.translate(str.maketrans(alphabet, alphabet[N:] + alphabet[:N]))
print(result)
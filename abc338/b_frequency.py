S = input()

most_frequent_character = "a"

for i in range(ord("b"), ord("z")+1):
    character = chr(i)

    if S.count(character) > S.count(most_frequent_character):
        most_frequent_character = character

print(most_frequent_character) 

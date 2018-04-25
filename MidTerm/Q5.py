vowels = ['a', 'e', 'i', 'o', 'u']
lst = []

user = input()

for char in user:
    if char in vowels:
      lst.append(char)

print (lst)
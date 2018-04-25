def findVowels(user):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = []

    for char in user:
        if char in vowels:
            lst.append(char)
    return lst

print (findVowels('apple'))
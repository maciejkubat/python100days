def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    name1 = name1.lower()
    name2 = name2.lower()
    names = name1 + name2
    for letter in names:
        if letter in "true":
            true_score += 1
    for letter in names:
        if letter in "love":
            love_score += 1
    true_love = str(true_score) + str(love_score)
    print(true_love)

calculate_love_score("Kanye West", "Kim Kardashian")
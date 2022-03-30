from random import choice

answers = ["Yes", "No", "Of Course Not", "Of Course Yes", "I think so", "I think Not"]


for i in range(5):
    ask = str(input("ASK SOMETHING: "))
    if ask.isalpha() != True and not '?' in ask:
        print("HEY, DO IT A QUESTION PLEASE")
        continue
    else:
        print(choice(answers))

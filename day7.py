import random

lives=6


random_word_list=["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon"]
random_word= random.choice(random_word_list)
print(random_word)

placeholder=""
word_length=len(random_word)

for position in range(word_length):
    placeholder +="_"
print(placeholder)

game_over=False
correct_letter=[]

while not game_over:
    first_guess=input("guess a letter from the world: ").lower()
    display=""
    for letter in random_word: 

        if letter == first_guess:
            display += first_guess
            correct_letter.append(first_guess)

        elif letter in correct_letter:
            display += letter   
        else:
            display += "_"

    print(display)

    if first_guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over=True
        print("you win")

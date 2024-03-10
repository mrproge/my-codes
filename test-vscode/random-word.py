import random

name = input("Whats your name? ")

words = ['programming' ,'science' ,'computer' ,'python'
         ,'mathematics' ,'player' ,'condition' ,'water' 
         ,'door' , 'satellite' , 'airplane' ,'board' ]

word = random.choice(words)

print("hads bezan: ")

guesses=''

turns=12

while turns > 0 :
    faild=0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")

            faild += 1

        if faild == 0:
            print("You win! ","The word is: " ,word)
            break
    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
    if guesses == 12:
        print("You loose!")







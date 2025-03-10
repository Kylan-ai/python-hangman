import random

#Basic variables needed.
hangman = [r'''           
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["gay", "lesbian", "bisexual", "transgender", "queer", "nonbinary", "pansexual", "omnisexual", "agender", "demiboy", "demigirl", "demisexual", "demiromantic", "asexual", "aromantic"]
random_word = random.choice(word_list)
word_dashes = "_" * len(random_word)
word_guesses = list(word_dashes)

#The introduction to the game.
print("Hello player! Welcome to a basic hangman game!")
response = input("Do you know how to play hangman? (Yes/No) ")
while True:
    if response.lower() == "yes":
        print("Of course you know how to play hangman. It's not that complicated.")
        break
    elif response.lower() == "no":
        print("""Alright, it's pretty simple.
You will be given how many letters are in a random word from my list of random words.
Then you will get # chances to guess correct letters.
When you guess a correct letter, it will be filled in on the spaces for the random word
If you guess an incorrect word, then you will progress the hangman.
If you finish the hangman, well, you kill the man. (I know, gruesome.) And you lose."
If you fill out the word, or guess the word, then you win!""")
        break
    else:
        print("This is not a valid reponse.")
        response = input("Please try again... (Yes/No) ")
print("Okay, let's get started!")

#The start of the actual games.
fails = 0
failed_guesses = []
correct_guesses = []

#A loop until the fails is the amount of fails there are in the hangman variables, which is the amount of wrong attemps that can happen.
while fails < len(hangman[fails]):
    print(hangman[fails])
    print(*word_guesses)
    guess = input("Please guess a letter: ")
    isLetter = guess.isalpha()
    #Checks if the person has already guesses the letter.
    if guess.lower() in word_guesses:
      print("You've already guessed that letter.")
    #Checks if the input was actually a letter.
    elif isLetter == False:
       print("You can only guess letters of the English alphabet.")
    #Checks if the correct word was chosen, which will end the game instantly.
    elif guess.lower() == random_word:
      print("You've guessed the correct word!")
      break
    #Checks to make sure the guess isn't longer than a single character.
    elif len(guess) > 1:
        print("You can only guess one letter at a time.")
    #This is when a letter is actually in the random word.
    elif guess.lower() in random_word:
      print("Correct!")
      correct_guesses.append(guess)
      #This is how it replaces the dashes with the guessed letters.
      word_guesses = [c if c in correct_guesses else "_" for c in random_word]
      #When all of the letters have been guessed, it will break the loop to take you to the end of the game.
      if "_" not in word_guesses:
        break
    #This makes sure that you can't repeat letters.
    elif guess in failed_guesses:
       print("You have already tried this letter. Try again: ")
    #If the above doesn't happen, it is an incorrect guess, and it will add one to the fails.
    else:
      print("Incorrect.")
      fails += 1
      failed_guesses.append(guess.lower())
      print(*failed_guesses)

#This is how it is determined if you lost or won the game.
if fails == len(hangman[fails]):
   print("I'm sorry, you have lost. Your word was " + random_word + ".")
else:
   print("Congradulation! You win!")

end=input("Enter anything to close the program.") 
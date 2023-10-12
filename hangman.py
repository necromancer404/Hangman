#hangman game written in python
import random
word_list=["apple","car","banana","laptop"]
def choose_word():
	return random.choice(word_list)
def display_word(word,guessed_letters):
	display=""
	for letter in word:
		if letter in guessed_letters:
			display+=letter
		else:
			display+="_"
	return display
def hangman():
	word=choose_word()
	guessed_letters= []
	attempts= 3


	print("Welcome to Hangman\n created by necromancer")
	while True:
		print(display_word(word,guessed_letters))
		guess=input("Take a guess: \n").lower()
		if guess in guessed_letters:
			print("You Already guessed that alphabet")
		elif guess in word:
			guessed_letters.append(guess)
		else:
			guessed_letters.append(guess)
			attempts -=1
			print("That's incorrect! you have",attempts," attempts left")
		if display_word(word,guessed_letters)==word:
			print("Congratulations! That's correct.The word was",word)
			break
		if attempts ==0:
			print("Your attempts have finished and you have lost the game.")
			break
hangman()
		


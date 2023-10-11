#hangman game written in python
import random
word_list=["apple","car","banana","laptop"]
def choose_word():
	return random.choice(word_list)
def display_word(word,guessed_letter):
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


	print("Hangman")
	while True:
		print(display_word(word,guessed_letters))
		guess=input("Take a guess").lower()
		


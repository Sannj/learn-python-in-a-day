vocabs = {'computer': ['an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program','_ _ _ _ _ter'],
'desktop':['the working surface of a desk','_ _ _ _ _ op'],
'device':['a thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.', '_ _ _ ice']}


def list_all_words():
	print('\nThe vocab list is: \n')
	for key, value in vocabs.items():
		print(' {} ({})\n        - {}\n'.format(key, value[1], value[0]))


def new_word():
	try:
		word, definition, hint = input('\nEnter a new word in this format(word|definition|hint)  ').split('|')
		if word in vocabs:
			print('The word already exists in the vocab list. Try again.')
			new_word()
		else:
			vocabs[word] = [definition, hint]
			print('Added the word!')
	except ValueError:
		print('Please check your format')
	except:
		print('Something is fishyy!!')

def remove_a_word():
	word = input('Enter a word to remove\n')
	if word in vocabs:
		del(vocabs[word])
		print('Voila! Word deleted!')
	else:
		print('Whoops! The word you entered does not exist in the list.')


def test_yourself():
	score = 0
	want_to_quit = False
	for key, value in vocabs.items():
		while True:
			guess = input('\nGuess the word based on the definition: \n{}\n\nor[p]ass or[h]int or [q]uit\n'.format(value[0]))
			if guess == key:
				print('\nWohoo! You guessed the word right!')
				score += 1
				break
			elif guess =='p':
				print('The correct answer is {}.'.format(key))
				break
			elif guess == 'h':
				print('The hint is: {}'.format(value[1]))
			elif guess =='q':
				want_to_quit = True
			else:
				print('\nWhoops! You got that wrong :(')
		if want_to_quit:
			break
	print('You got {}/{}'.format(score, len(vocabs)))

def first_method():
	while True:
		choice = input("""\n\nWelcome to the Vocab Builder\n\nChoose an option from the menu:\n
			1) Test yourself
			2) Add a new word to the vocab list
			3) Remove a word from the list
			4) List all the words in the vocab list
			5) Quit\n""")
		if choice == "1":
			test_yourself()
		elif choice == "2":
			new_word()
		elif choice == "3":
			remove_a_word()
		elif choice == "4":
			list_all_words()
		elif choice == "5":
			break
		else:
			print('Invalid option. Try again.')
			first_method()



first_method()



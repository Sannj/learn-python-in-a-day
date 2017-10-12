vocabs = {'computer': ['an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program','_ _ _ _ _ter'],
'desktop':['the working surface of a desk','_ _ _ _ _ op'],
'device':['a thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.', '_ _ _ ice']}


def list_all_words():
	print('\nThe vocab list is: \n')
	for key, value in vocabs.items():
		print(' {} ({})\n        - {}\n'.format(key, value[1], value[0]))


def new_word():
	try:
		word, definition, hint = input('\nEnter a new word in this format(word|definition|hint)')
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

def remove_a_word:
	word = input('Enter a word to remove\n')
	if word in vocabs:
		del(vocabs[word])
		print('Voila! Word deleted!')
	else:
		print('Whoops! The word you entered does not exist in the list.')


def test_yourself():
	score = 0;
	for key, value in vocabs.items():
		guess = input('\nGuess the word based on the definition: {}'.format(value[0]))
		if guess == key:
			print('\nWohoo! You guessed the word right!')
		else:
			print('\nWhoops! You got that wrong :(')
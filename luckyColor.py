import random

def verify_color(color_chosen, colors):
	found = False
	for i in range(3):
		user_color = input('Enter your guess number {} '.format(i+1))
		if color_chosen == user_color:
			print('Wohooo!! You guessed it right!')
			found = True
			break
		else:
			print('Whoops! Try again!'.format(color_chosen))
			colors.remove(user_color)
			print('The list of colors left to guess are: '+str(colors))

	if found == False:
		print('Aww! Better luck next time. The lucky color was {}'.format(color_chosen))

intro = '''Hello people! Welcome to the guess the color application.
In this application, we are going to pick(using the in built random function) a secret color (from a static list) application for you. 
Then, we ask you to guess your lucky color and we will see if it matches the color the application chose for you. Let us see if you can guess the secret color right.'''

print(intro)

colors = ['red', 'blue', 'green', 'purple', 'yellow']

print('The list of colors are: '+str(colors))

print('You will have 3 tries to guess the secret color! Let us try your luck :)')

color_chosen = colors[random.randint(0, len(colors))]
verify_color(color_chosen, colors)




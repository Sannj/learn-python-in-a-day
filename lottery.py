import random

cash = 2000
first_time = True

def validate(lott_numbers):
	global cash
	user_numbers = set()
	numbers_as_string = input('Input the unique numbers separated only by a comma. Ex: 1,2,3,4,5,6\nThe range is 1 through 100. ')
	numbers_as_list = numbers_as_string.split(',')
	user_numbers = {int(n) for n in numbers_as_list}
	while (len(user_numbers)*100) > cash:
		print('You don\'t have enough cash. Please re-enter your lottery numbers.\n')
		numbers_as_string = input('Input the unique numbers separated only by a comma. Ex: 1,2,3,4,5,6\nThe range is 1 through 100. ')
		numbers_as_list = numbers_as_string.split(',')
		user_numbers = {int(n) for n in numbers_as_list}
	cash = cash - len(user_numbers)*100
	intersection_values = lott_numbers.intersection(user_numbers)
	len_intersection = len(intersection_values)
	if len_intersection == 3:
		cash = cash + 600
	elif len_intersection == 4:
		cash = cash + 1000
	elif len_intersection == 5:
		cash = cash + 1500
	elif len_intersection == 6:
		cash = cash + 10000
	else:
		print('Aww. You do not have enough matches! Hope it works out next time!')

	print('The lottery numbers were: '+str(lott_numbers))

	print('After this round you currently have ${}.'.format(cash))
	choice = input('Do you wish to play again? If yes press \'y\' else \'n\' ')
	if choice == 'y' or choice == 'Y':
		intro_module()
	else:
		print('Thank you for playing!')

def generate_lottery_numbers():
	lottery_numbers = set()
	while len(lottery_numbers) < 7:
		lottery_numbers.add(random.randint(1, 100))
	return(lottery_numbers)

def intro_module():

	global first_time
	intro = '''Welcome to the Lottery app! This is the ultimate test of your luck. You have a starting balance of $2000.
	\nThe lottery happens in the range of 1 to 100. You can buy any number of numbers as long as you have cash. You need to pay $100 for each number.
	\nIf you match 3 numbers you get $600, for 4 numbers you get $1000, for 5 numbers you get $1500
	and if all the 6 colors match you get $10,000. So let us see if you win some money.'''

	if first_time:
		print(intro)
		first_time = False

	lottery_numbers = generate_lottery_numbers()
	validate(lottery_numbers)


intro_module()



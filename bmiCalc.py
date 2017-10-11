def calBMI(h, w):
	bmi = int(w)/(int(h)/100)**2
	print('Your BMI is: {}'.format(round(bmi, 2)))
	bmi = round(bmi, 2)
	if bmi > 25:
		print('You have this sweetheart! You can get rid of those extra pounds!')
	elif bmi < 18.5:
		print('Omg. You need Nutella like right now! You need more pounds.')
	else:
		print('Keep maintaining this!')

print('Hello! Welcome to the best BMI calculator in this world :P\nNow you will be prompted to enter a few values and then your BMI will be displayed! \nWohoo!')
height = input('Now, enter your height in centimeters ')
weight = input('Awesome! Now enter your weight in kilograms please. ')
print('The computer is calculating your BMI. Hold on tight!\n')
for x in range(5):
	for y in range(x+1):
		print('.', end='')
	print('\n')
calBMI(height, weight)







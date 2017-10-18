import random
import time

class Witch:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def __repr__(self):
		return('{}(lvl{})'.format(self.name, self.level))

	def witch_attack(self):
		witch_damage = random.randint(1, 10) * self.level
		return witch_damage


#A fire witch may or may not have a fire staff
class FireWitch(Witch):
	def __init__(self, name, level, fire_staff):
		super().__init__(name, level)
		self.fire_staff = fire_staff
	# def __repr__(self):
	# 	print('{}(lvl{})'.format(self.name, self.level))
	def witch_attack(self):
		base_attack = super().witch_attack()
		if self.fire_staff:
			print('You are fighting a Fire Witch!!')
			base_attack = base_attack * 2
			return base_attack
		else:
			return base_attack

#An Evil Witch will always have a black staff
class EvilWitch(Witch):
	def __init__(self, name, level, black_staff_level):
		super().__init__(name, level)
		self.black_staff_level = black_staff_level
	# def __repr__(self):
	# 	print('{}(lvl{})'.format(self.name, self.level))
	def witch_attack(self):
		base_attack = super().witch_attack()
		print('You are being attacked by an Evil Witch with a Black Stack Level: {}'.format(self.level))
		return base_attack * 2 * self.black_staff_level

class Hunter:
	def __init__(self, name, level):
		self.name = name
		self.level = level
	def __repr__(self):
		return('{}(lvl{})'.format(self.name, self.level))

	def hunter_attack(self, witch, critical_strike):
		base_damage = random.randint(1, 10) * self.level
		# if critical_strike:
		# 	hunter_damage = base_damage * 2
		# else:
		# 	hunter_damage = base_damage
		hunter_damage = base_damage * 2 if critical_strike else base_damage
		witch_damage = witch.witch_attack()
		critical_strike_msg = '(critical_strike!)' if critical_strike else ''
		print('You attacked {}. {}'.format(hunter_damage, critical_strike_msg))
		print('Witch attacked {}'.format(witch_damage))

		if hunter_damage > witch_damage:
			print('You defeated the {}'.format(witch.name))
			return True
		else:
			print('Whoops! {} successfully ran away!'.format(witch.name))
			return False


def start_game():
	hunter = Hunter('hunter', 1)
	while True:
		witches=[Witch('witch', random.randint(1,5)), FireWitch('firewitch', random.randint(6,20), random.choice([True, False])),
		EvilWitch('EvilWitch', random.randint(21,30), random.randint(1,3))]
		witch = random.choice(witches)
		print('\n{} has appeared!!\n'.format(witch))
		cmd = input('Do you [a]ttack or [s]top tracing or [q]uit? ')
		if cmd == 'a':
			if hunter.hunter_attack(witch, random.choice([True, False])):
				hunter.level = hunter.level + 1
				print('Level Up!')
			else: 
				print('Hunter is recovering!')
				time.sleep(1)
		elif cmd == 'q':
			break
		else:
			print('Hunter stopped tracing this Witch')

start_game()



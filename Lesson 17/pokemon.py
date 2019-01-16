import time
import random

print()
print('-' * 65)
print('A wild Evee appears!')
time.sleep(0.2)
print('You only have one Pokemon, Umbreon.')
time.sleep(0.2)
print('I choose you Umbreon!!!!!')
print()
time.sleep(0.2)

Umbreon_hp = 200
Evee_hp = 125

print('Battle Options:')
time.sleep(0.2)
print('- (1) Sleep Heal')
time.sleep(0.2)
print('- (2) Tackle')
time.sleep(0.2)
print('- (3) Roundhouse Kick')
time.sleep(0.2)
print('- (4) Hyperbeam')
your_move = input('Choose a move using the corresponding number: ')
if your_move == '1':
	print('Umbreon uses Sleep Heal')
	Umbreon_hp = Umbreon_hp + 50
	print('Umbreon uses Sleep Heal, his HP increases to ' + str(Umbreon_hp))
	time.sleep(0.2)
elif your_move == '2':
	Evee_hp = Evee_hp - 10
	print('Umbreon uses Tackle and deals 10 damage to Evee!')
	time.sleep(0.2)
elif your_move == '3':
	evee_hp = evee_hp - 30
	print('Umbreon uses Roundhouse Kick and deals 30 damage to Evee!')
	time.sleep(0.2)
elif your_move == '4':
	Evee_hp = Evee_hp - 40
	print('Umbreon uses Hyperbeam and deals 40 damage to Evee!')
	time.sleep(0.2)


enemy_move = random.randint(1,2)
enemy_move = str(enemy_move)

if enemy_move == '1':
	Umbreon_hp = Umbreon_hp - 30
	Evee_hp = Evee_hp + 30
	print('Evee uses Drink Blood and deals 30 HP and restores 30 HP!')
	time.sleep(0.2)
elif enemy_move == '2':
	Umbreon_hp = Umbreon_hp - 50
	print('Evee uses Breathe Fire and deals 50 HP!')
	time.sleep(0.2)
print()
capture_roll = random.randint(0,125)
if capture_roll > Evee_hp:
	print('You have captured Evee!')
	break
else: 
	print('You tried to capture Evee, but it escaped!')

if Umbreon_hp < 0:
	Umbreon_hp = 0
if Evee_hp < 0:
	Evee_hp = 0

print('Updated HP!')
time.sleep(0.2)
print('- Umbreon HP: ' + str(Umbreon_hp))
time.sleep(0.2)
print('- Evee HP: ' + str(Evee_hp))
time.sleep(0.2)
print()
time.sleep(0.2)

if Umbreon_hp == 0:
	print('Umbreon has been defeated! Evee wins!')
elif Evee_hp == 0:
	print('Evee has been defeated! You win!')

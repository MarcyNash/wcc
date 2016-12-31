import random

#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(cards) # To see the list before being shuffled

random.shuffle(cards)

#print(cards) # To see the list after being shuffled
#print("")
#print("")

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Your card: ' + str(player_card1))
print('Computer card: ' + str(computer_card1))

#print(cards) # To see the list after two cards have been popped off.


# Note  - GetHitOrStay() should be a method returning 's' or 'h'
# the default will be 's'

# In Round 2, both Player and Computer can hit (draw another card) or stay (not draw). In Round 2, the Computer always hits.
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
	player_card2 = cards.pop()
	player_card_output_string = ", " +  str(player_card2)
else:
	player_card2 = 0
	player_card3 = 0	# player also stays (not draw) in Round 3
	player_card_output_string = ""
	
# Computer always draws a card in Round 2
computer_card2 = cards.pop()

print('Your cards:  ' + str(player_card1)  + player_card_output_string)
print('Computer cards:  ' + str(computer_card1) + ", " +  str(computer_card2))

#print(cards) # To see the list after next two cards have been popped off.

# In Round 3, both Player and Computer can hit (draw another card) or stay (not draw). In Round 3, the Computer only hits if their cards add up to less than 16.
if decision == 'h':
	decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

	if decision == 'h':
		player_card3 = cards.pop()
		player_card_output_string = player_card_output_string + ", " +  str(player_card3)
	else:
		player_card3 = 0

	
if (computer_card1 + computer_card2) < 16:
	computer_card3 = cards.pop()
	computer_card3_output = ", " + str(computer_card3) 
else:
	computer_card3 = 0;
	computer_card3_output = ""

print('Your cards:  ' + str(player_card1)  + player_card_output_string)
print('Computer cards:  ' + str(computer_card1) + ", " +  str(computer_card2) + computer_card3_output)

player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

#print("Player total = " + str(player_total))
#print("Computer total = " + str(computer_total))

print("")
print("Game over...")
if player_total > 21 and computer_total > 21:
	print("Tied. (You and computer busted)")  # player and computer over 21
elif player_total > 21:
	print("Computer wins! (You busted.)")  # player over 21
elif computer_total > 21:
	print("You win! (Computer busted)")  # computer over 21
elif player_total > computer_total:
	print("You win! (You were closest to 21.)")
elif player_total == computer_total:
	print("Tied! (You and the computer both  got " + str(player_total) + ".)")
else:
	print("Computer wins. (It was closest to 21.)")


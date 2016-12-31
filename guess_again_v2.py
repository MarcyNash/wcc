import random

# Using constants to set the range allows us to change to other numbers besides 1 and 100. 
# All print statements now use these constants rather than 1 and 100. Using constants also 
# allows us to do a range check on the player's guesses.
START_NUMBER = 1
STOP_NUMBER = 100

# Set a constant to the maximum number of guesses allowed. This allows us to easily change the number
# of guesses in a game.
MAX_GUESSES = 5

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

	# Get initial guess
	guess = raw_input('Enter your guess: ')

	# Assume it's not valid, until it's proven otherwise
	valid = False

	while valid != True:

		try:
			# Try and convert this number to an integer
			# If it fails, the exception will occur
			guess = int(guess)
			
			if guess < START_NUMBER or guess > STOP_NUMBER:
				raise Exception
		
		except Exception:
			# Exception was thrown when trying to convert to number,
            # Report the issue and ask again
			print("Invalid input; please enter a whole number between " + str(START_NUMBER) + " and " + str(STOP_NUMBER) + ".")
			valid = False
			guess = get_guess()

		# If they get here, it means the number must have been valid
		# Set valid to be true to break out of the while loop
		valid = True

	return guess

# Test get_guess
#print get_guess() # Expected: Keeps prompting until user enters a valid number

def compare(numA, numB):
	
	if numA > numB:
		return 'high'
	elif numA < numB:
		return 'low'
		
# Test compare
#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'low'
#print compare(99,100) # Expected: 'low'

def play():

	# Pick a secret number
	secret_number = random.randint(START_NUMBER,STOP_NUMBER)

	# When building your program, the following line will tell you what
	# the secret_number is; this will make it easier to test the game.
	# When done, remove or comment-out this line.
	print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))
	
	# Assume the player looses
	winner = False
	
	# Print message at the start the game
	print("\nI'm thinking of a number between " + str(START_NUMBER) + " and " + str(STOP_NUMBER) + "; what do you think it is?")

	# Get the player's initial guess
	player_guess = get_guess()
	
	
	# Only allow 5 guesses; first guess is above the for loop. Once in for loop player has only 4 guesses left
	for guess_count in range(1, MAX_GUESSES):
		
		if player_guess == secret_number:
			# Print conclusion
			print('You got it! The number was ' + str(secret_number) + ".")
			winner = True
			break;
			
		# For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'
		compare_guess = compare(player_guess,secret_number)
		# Use 'guess' if the player guesses on the first try or has 1 guess left. 
		guess_string = " guesses"		
		if MAX_GUESSES-guess_count == 1:
			guess_string = " guess"
		print("Too " + compare_guess + "; you have " + str(MAX_GUESSES-guess_count) + guess_string + " left.")
		
		# Get the player's initial guess
		player_guess = get_guess()
	
	if 	winner == False:
		print("Sorry, you ran out of turns! The correct number was " + str(secret_number) + ".")
				
# Run the game
play()

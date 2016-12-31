# Import statements should always be at the top of your file, not in the body of functions
import random

def multiply(a, b):
    result = a * b
    return result
	
def isPositive(a):
    if a > 0:
        return True
    else:
        return False
		
def draw_random_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    random.shuffle(cards)
    return cards.pop()


def display_winner(winner, msg):
    if winner == 'Player':
        outcome = 'You win! '
    else:
        outcome = 'Computer wins! '

    print(outcome + '(' + msg + ')')

# Test the display_winner function
#display_winner('Player', 'You were closest to 21') # Expected: You win! (You were closest to 21)
#display_winner('Computer', 'It was closest to 21') # Expected: Computer wins! (It was closest to 21)
#display_winner('Computer', 'You busted')  # Expected: Computer wins! (You busted)		
	
# Test the draw_random_card function
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
				
# Test the multiply function:
#print(multiply(4,5)) # 20
#print(multiply(9,11)) # 99
#print(multiply(0,10)) # 0
#print(multiply(.5,9)) # 4.5
#print(multiply(-1, -55)) # 55
#print(multiply(3, 'Hello')) # 'HelloHelloHello'
		
# Test the isPositive function
#print(isPositive(-4)) # Expected: False
#print(isPositive(4)) # Expected: True
#print(isPositive(-9.9)) # Expected: False
#print(isPositive(9.9)) # Expected: True


def mystery(x, y, z):

    # ??? Your code here 
	return(x + (y * z))
	
	
# Test this function:
#print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
#print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculate_tip(meal_price, rating): # float:meal_price, string:rating
	
	# Set tip percentage based on rating
	if rating == 'A':
		percentage = .20
	elif rating == 'B':
		percentage = .18
	elif rating == 'C':
		percentage = .15
		
	return float(meal_price) * percentage
	
	
print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4

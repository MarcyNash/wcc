#name = raw_input('What is your name? ')
#print('Hi ' + name)

#name = raw_input('What is your name?')
#age = raw_input('How old are you?')
#print(name + ' is ' + age + ' years old.')
#dog_years = int(age) * 7
#print('You are ' + str(dog_years) + ' old in dog years.')


meal_cost = raw_input('How much was your meal? ')
tip = float(meal_cost) * .20
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(float(meal_cost) + tip))
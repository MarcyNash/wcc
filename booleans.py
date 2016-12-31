#Complete the print function in the following code, so that it would print True if the entered age was between 5 and 10.

#Your expression should be inclusive, which means it should include 5 and 10 in the range of acceptable values.


age = int(raw_input('How old are you? '))
#print(age >= 5 and age <= 10)
#print(age == 5 or age == 10 or (age > 5 and age < 10))
#print(age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10)

print(age > 5 and age < 10)
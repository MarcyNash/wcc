print("Welcome to the Mad Lib Generator!")
print("")
print("")


# Get words from the user
first_adjective = raw_input("Type in an adjective:  ")  #fearless
second_adjective = raw_input("Another adjective: ")  #gooey
third_adjective = raw_input("And another adjective: ")  #sassy
fourth_adjective = raw_input("One more adjective: ")  #fancy
plural_animal = raw_input("Plural animal (e.g., puppies): ")  #elephants
verb = raw_input("Now a verb: ")  #skip
plural_noun = raw_input("Now a plural noun: ")  #marbles
woman_musician = raw_input("The first name of a woman musician: ")  #Ani
beverage = raw_input("A beverage: ")  #chocolate milk
plural_body_part = raw_input("And finally, a plural body part: ")  #knees
print("")

# Write the story with the words gotten from the user.
print("Excellent choices! Here's your story...")
print("--------------------------------")
print("There once was a " + first_adjective + " programmer named " + woman_musician)
print("who wanted to build a " + second_adjective + " mobile app to")
print("help " + third_adjective + " " + plural_animal + " find new homes.")
print("")
print(woman_musician + " stayed up all night, drinking lots of")
print("caffeinated " + beverage + " as she worked and worked")
print("trying to complete her " + fourth_adjective + " program.")
print("")
print("Whenever " + woman_musician + " hit a dead end, she would")
print("exclaim *" + plural_noun + "*!")
print("")
print("But she was not discouraged, and after a quick break")
print("to " + verb + " and clear her head, she got back to work.")
print("")
print("By morning, when the sun started to rise, she let out a")
print("big yawn and stretched her " + plural_body_part + ".")
print("Finally, she was done.")
print("--------------------------------")
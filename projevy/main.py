# Welcome & Description of Project

username = input("What should I call you?   ")

print()

print("Welcome,", username,", to your Storyline Revision Organizer.")

print()

print("With this guide, you'll be asked questions regarding the story you've read about. As you answer said questions, it'll better your memory and understanding of what you've read.")

# The list of things you can do

print()
print()

print("Edit--This will allow you to write in the section you choose.")
print("View--This allows you to view what you have written in whichever section you choose.")
print("Clear--This will clear everything you have written, but only in the section of your choosing.")
print("Clear All--This clears all your writing and starts you from the beginning.")

# MEnU = ["edit", "view", "clear all", "clear"]

# Maybe a little picture




# Finally, show list and ask user what they would like to do

print()
print()

print("Edit")
print("View")
print("Clear")
print("Clear All")

print()

print("What would you like to do?")

choice = input(" ")

choice = choice.lower()

# What choosing edit leads to

if choice == "edit":
    print("What would you like to edit?")
    print("Choose a number between 0 and 20(including '0')")

# Choices of what they can edit and how to end it

print("Prompts:")

print()

questions = ["1. Explain the title.", "2. What category or genre do you think it fits into?", "3. What do you think the author's purpose was?", "4. Something you liked about it.", "5. Something you disliked about it.", "6. Describe the setting.", "7. Which character did you like most?", "8. Which character did you like least?", "9. Describe one of the main characters.", "10. What changes does a main character go through?", "11. Describe one significant episode.", "12. What techniques does the author use to tell the story?", "13. How did reading it change you, or your views?", "14. What would you say to persuade a friend to read it or not to read it?", "15. Summarise it in one written sentence or a one minute speech.", "16. What feedback would you give the author?", "17. How might you have written it differently?", "18. What do you think of the ending?", "19. What happens, or should happen, after the ending?", "20. What would you want to read about in a sequel or prequel?"]

answers = []

while True:
    choice2 = input("")
    if choice2.isnumeric() == False:
        print("Has to be a number! Here, try again!")
    else:
        print(questions[choice2])
        break

# Make a spot for user to edit

print("Begin writing below:")

usersedit = input("")

answers.append(usersedit)

print()

print(questions[choice2], answers)

print("")

print("Would you like to quit?  Yes or No?")

choice1 = input("")

choice1 = choice1.lower()

# if choice1 == "no":
    









# Clear option 

# Tell user what it does

# Ask user if they wish to proceed

# If user wished to proceed, Clear all

# Repeat everything, but asking for username and welcome statement

#2.7 Performance Assessment Decisions, Loops, Processing, Output Formatting
#Name: Gabriela Balanta
#Date: 09-19-2026
#Descrition: this is a program that lets the user try to guess a number between 1 and 10

#prompts user for name and student id
name = input("What is your name? ") 
stuId = input("What is your studentID? ")

#variables used to keep track of guesses and tries
rightGuess = 5
tries = 0

while True:
    userGuess = int(input("Please guess a number between 1 and 10..."))
    tries += 1
    
    if  userGuess > rightGuess:
        print("You guessed too high")
    elif userGuess < rightGuess:
        print("You guessed too low")
    else:
        print(f"Congratulations, {name}!")
        print(f"You guessed the number in {tries} tries!")
        break

#shows the output from a whlie loop
print("\nOutput from the 'while' loop:")

count = 0

while count < 5:
    incrementValue = rightGuess + count + 1
    print(f"{rightGuess} incremented by {count +1 } is {incrementValue}")
    count += 1
    
#shows the output from a for loop
print("\nOutput from the 'for' loop:")

for count in range(5):
    incrementValue = rightGuess + count + 1
    print(f"{rightGuess} incremented by {count + 1} is {incrementValue}")
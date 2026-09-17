#1.9 Performance Assessment Data Types and Basic Math Operators
#Name: Gabriela Balanta
#Date: 09-17-2026

#prompts student to neter their name and ther student id
student = input("Please enter your name: ")
stuId= input("Please enter your Student ID: ")

#promts the user to enter 2 different whole numbers
num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter a different whole number: "))

#used to perform the basic math operations with the two user given numbers
mul= num1 *num2
div= num1/num2
add= num1 + num2

#shows the results of the math operations
print(f"The result of {num1} times {num2} is: {mul:.2f}")
print(f"The result of {num1} divided by {num2} is: {div:.2f}")
print(f"The result of {num1} plus {num2} is: {add:.2f}")

#if else statement that shows which of the two numbers is larger
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num1 < num2:
    print(f"{num2} is larger than {num1}")
    
# shows the student name and id
print(student)
print(stuId)
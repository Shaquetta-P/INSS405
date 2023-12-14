print ("Welcome To SWJ Pop Quiz Game!")
print ("Created By: S.Phillips, W. Jackson, J. Patton")
import math
print("__________________________________________________")
question1 = ("1." "What is the name of the first president of the United States?:")
print(question1)
response_q1 = input("Enter Answer: ")
response_q1 = response_q1.upper()
if response_q1 == ("GEORGE WASHINGTON"):
    print("Correct")
else:
    print("Incorrect")
print("__________________________________________________")

question2 = ("2. Finish the number count: 2, 5, 8, 11 _____ ")
print(question2)
expected_numbers = [14, 17, 20, 23]

user_attempts = 2
attempts = 0

while attempts < user_attempts:
    try:
        response_q2 = [int(input("Please enter the next number: " )) for _ in range(4)]

        if response_q2 == expected_numbers:
            print("Correct")
            break # Exit the loop if the input data type is correct
    except ValueError:
        print("Invalid input." )
    else:
        print("Incorrect")

    attempts += 1
print("__________________________________________________")

question3 = ("3." "What is 4 to the 5 power?: ")
print(question3)

choices = ["A. 1102","B. 1091","C. 1024","D. 1022"]
for item in choices:
    print(item)

answer_q3 = ("C")
response_q3 = input("Enter your answer A, B, C, or D: ")

response_q3 = response_q3.upper()


if answer_q3 == response_q3:
    print("Correct: C. 1024")
else:
    print("Incorrect")


print("__________________________________________________")

question4 = ("4." "What year did World War III start?:")
print(question4)
response_q4 = input("Enter Answer: ")
if response_q4 == ("1942"):
    print("Correct")
else:
    print("Incorrect")

print("__________________________________________________")

question5 = ("5." "What is 5 X 10")
print(question5)
answer_1 = input("a)50\nb)60\nc)35\nd)34\n:")
if answer_1.lower() == "a" or answer_1.lower() == "50":
    print("Correct")
else:
    print("Incorrect, 5 x 10 is 50")

print("__________________________________________________")

question6 = ("6. Which document outlined the original framework of the United States government?: ")
print(question6)

Choices = ["A. Declaration of Independence", "B. Constitution", "C. Bill of Rights"]

for item in Choices:
    print(item)
answer_q6 = ("B")
response_q6 = input("Enter your answer A, B, C, or D: ")

response_q6 = response_q6.upper()

if response_q6 == ("B"):
    print("Correct")
else:
    print("Incorrect")

print("__________________________________________________")

question_7 = "7.” “What is the result of 5 + 7?"

print(question_7)

answer_q7 = ["A. 10", "B. 12", "C. 15"]

for item in answer_q7:
    print(item)

answer_q7 = "B"

response_q7 = input("Enter your answer A, B, or C: ")

response_q7 = response_q7.upper()

if response_q7 == answer_q7:

    print("Correct")

else:

    print("Incorrect")
print("__________________________________________________")

print("__________________________________________________")

print("       THANK YOU FOR PLAYING !!!    ")

print("__________________________________________________")
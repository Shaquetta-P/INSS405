import random

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(number, 'Tic Tac')
elif number % 3 == 0:
    print(number, 'Tic')
elif number % 5 == 0:
    print(number, 'Tac')

counter = 1
while counter <= 20:
    print(counter)
    counter += 1

counter = 1
while counter <= 20:
    if counter % 3 == 0 and counter % 5 == 0:
        print(counter, 'Tic Tac')
    elif counter % 3 == 0:
        print(counter, 'Tic')
    elif counter % 5 == 0:
        print(counter, 'Tac')
    counter += 1

random_number = random.randint(1, 100)
print("Random Number:", random_number)

attempts = 0
while attempts < 5:
    user_value = int(input("Enter a value greater than 0: "))
    if user_value > 0:
        break
    else:
        print("Value must be greater than 0. Try again.")
        attempts += 1

if user_value == random_number:
    print("Perfect Match!")
else:
    print("Numbers don't match. Random:", random_number, "User:", user_value)

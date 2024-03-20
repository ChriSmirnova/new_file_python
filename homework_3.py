number_1 = int(input("Say whole number from 1 to 10?"))
number_2 = 2
multiply_action = number_1 * number_2
divide_action = number_1 / number_2
plus_action = number_1 + number_2
multiply_action = number_1 - number_2
if number_1 in (2,4,6):
    print(multiply_action)
elif number_1 in (8,10):
    print(divide_action)
elif number_1 in (1,3,5):
    print(plus_action)
elif number_1 in (7,9):
    print(minus_action)
else:
    print("The number is not recognized.Try again!")


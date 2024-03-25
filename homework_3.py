operation = input("Which operation you want use +, -, /, *?")
number_1 = int(input("Say first number?"))
number_2 = int(input("Say second number?"))
if operation == '+' :
    result_1 = number_1 + number_2
    print(result_1)
elif operation == '-' :
    result_2 = number_1 - number_2
    print(result_2)
elif operation == '/':
    result_3 = number_1 / number_2
    print(result_3)
elif operation == '*':
    result_4 = number_1 * number_2
    print(result_4)
else:
    print("Try again!")


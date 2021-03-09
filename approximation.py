number = 100000                                              # the desired number to be found
input_number = input_number2 = 0.00                         # approximation of what the number could be
increments = 1                                           # what increments to search for desired number with

while input_number != number and input_number2 != number:   # check if input is desired number
    input_number = round(input_number, 2)                   # round the numbers to make decimal guessing possible
    input_number2 = round(input_number2, 2)
    number = round(number, 2)
    increments = round(increments, 2)

    input_number = input_number + increments                #approximating desired number in positive direction
    input_number2 = input_number2 - increments              #approximating desired number in negative direction
    print("Input1: ", input_number)                         #print progress of approximation
    print("Input2: ", input_number2)
    if input_number == number:                              #check result
        print("The Number is: ", round(input_number))       #print result
    if input_number2 == number:
        print("The Number is: ", round(input_number2))

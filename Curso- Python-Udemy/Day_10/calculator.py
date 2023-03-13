from replit import clear
from art import logo 
print(logo)
print("\n")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
}

run = True
while run == True:
    
    numb_1 = float(input("Type the first number: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick Up a operation from the list above: ")

    numb_2 = float(input("Type the second number: "))

    function = operations[operation_symbol]
    result = function(numb_1, numb_2)

    print(f"{numb_1} {operation_symbol} {numb_2} = {result}")

    run_ag = input("Want to do another operation? (y/n): ")
    if run_ag == "y":
        run 
        clear()
    elif run_ag == "n":
        run = False
    else:
        print("Invalid Option.")
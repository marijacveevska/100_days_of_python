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
    "/": divide, 
    }


def calculator():
    should_restart = True
    print("C A L C U L A T O R")
    x1 = float(input("What is the first number? "))

    while should_restart:
        
        operant = input(" Pick an operation: \n" \
        "+ \n" \
        "- \n" \
        "* \n" \
        "/ \n")
        x2 = float(input("What is the next number? "))
        y = operations[operant](x1,x2)
        print(f"{x1} {operant} {x2} = {y}")


        Q_continue = input(f"Type 'y' if you want to continue with {y}, or type 'n' if you want to start a new calculation ")
        if Q_continue == "y":
            x1 = y
        else:
            should_restart = False
            print("\n"* 3)
            calculator()


calculator()
    





# Warning: This code is intentionally bad. Do not use in real projects.

import time

def megaUltraCalculator(a, b, operation):
    # Just to make sure it's slow
    for i in range(10000000):
        pass

    if operation == "+":
        return a + b
    elif operation == "-":
        for _ in range(100000):
            pass  # Useless loop
        return a - b
    elif operation == "*":
        result = 0
        for _ in range(b):  # Reinventing the wheel
            result += a
        return result
    elif operation == "/":
        if b == 0:
            print("Oops! Division by zero. Let's just give you a random number.")
            return 42  # Arbitrary result
        else:
            # Overcomplicated division
            return sum([a / b for _ in range(1)])  
    else:
        print("Unknown operation, but who cares? Here's 0.")
        return 0


def main():
    print("Welcome to the Worst Calculator Ever!")
    time.sleep(2)  # To make it slower and annoying
    print("Calculating takes time, please wait...")
    
    # User input (with no validation)
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Call the worst function ever
    result = megaUltraCalculator(a, b, operation)
    
    print("Your result is:", result)
    print("Have a painful day! :)")

if __name__ == "__main__":
    main()

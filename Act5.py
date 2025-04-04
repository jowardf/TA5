def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()
        #Quit program
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        #Divide, Exponent, Remainder function
        if choice in ['D', 'E', 'R']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid integers.")
                continue

            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
        #Summation function
        elif choice == 'F':
            try:
                start = int(input("Enter the starting number: "))
                end = int(input("Enter the ending number: "))
            except ValueError:
                print("Error: Please enter valid integers.")
                continue

            result = summation(start, end)

        else:
            print("Invalid choice. Please try again.")
            continue

        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()

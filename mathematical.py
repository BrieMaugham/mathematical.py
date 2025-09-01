def calculator():
    """Perform arithmetic operations on floats and integers."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Choose an operator (+, -, *, /, %): ").strip()
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif operator == "%":
                result = num1 % num2 if num2 != 0 else "Error: Modulus by zero"
            else:
                result = "❌ Invalid operator. Choose from +, -, *, /, %."

            print(f"✅ Result: {result}\n")

            # Ask if user wants to calculate again
            again = input("Do you want to calculate again? (y/n): ").strip().lower()
            if again != "y":
                print("👋🏾 Exiting calculator...")
                break
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.\n")

def main():
    print("🔢 SIMPLE CALCULATOR\n")
    calculator()

if __name__ == "__main__":
    main()

"""
mathematical.py
An interactive calculator for both integers and floats using basic arithmetic operators.

Author: Bridie Maugham Dibora
"""

def view_profile():
    """Display user's professional profile."""
    print("\n👤 PROFILE")
    print("=" * 50)
    print("Full Name     : Bridie Maugham Dibora")
    print("Role          : Digital Creative & Web Developer")
    print("Email         : maughamdiborapr@gmail.com")
    print("Phone         : +254 701170131")
    print("Specialties   : HTML5, Accessibility, Branding, SEO, Social Media")
    print("=" * 50 + "\n")


def show_help():
    """Show help instructions for the calculator."""
    print("\n🆘 HELP GUIDE")
    print("=" * 50)
    print("This program is a simple calculator that supports:")
    print("  ➕ Addition       (e.g., 5.5 + 2)")
    print("  ➖ Subtraction    (e.g., 7 - 3.2)")
    print("  ✖️ Multiplication (e.g., 4 * 2.0)")
    print("  ➗ Division       (e.g., 8.2 / 2)")
    print("  🧮 Modulus        (e.g., 9.5 % 4)")
    print("Inputs can be whole numbers or decimal numbers.")
    print("=" * 50 + "\n")


def calculator():
    """Perform arithmetic operations on floats and integers."""
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
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.\n")


def main():
    """Main dashboard loop."""
    print("🔢 FLEXIBLE CALCULATOR (FLOAT & INTEGER)")

    view_profile()
    show_help()

    while True:
        print("📋 MENU")
        print("1. Use Calculator")
        print("2. View Profile")
        print("3. Help Guide")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        match choice:
            case "1":
                calculator()
            case "2":
                view_profile()
            case "3":
                show_help()
            case "4":
                print("👋🏾 Exiting... See you again!")
                break
            case _:
                print("❌ Invalid option. Please select 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()

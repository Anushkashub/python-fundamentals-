import json
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses
try:
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
except:
    expenses = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Highest Expense")
    print("7. Lowest Expense")
    print("8. Monthly Summary")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: ₹"))

        expense = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount
        }

        expenses.append(expense)
        save_data()

        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":
        if expenses:
            print("\n--- Expense List ---")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['Date']} | "
                    f"{expense['Category']} | "
                    f"₹{expense['Amount']}"
                )
        else:
            print("No Expenses Found!")

    # Total Expense
    elif choice == "3":
        total = sum(expense["Amount"] for expense in expenses)
        print(f"\nTotal Expense: ₹{total}")

    # Search Category
    elif choice == "4":
        category = input("Enter Category: ")

        found = False

        for expense in expenses:
            if expense["Category"].lower() == category.lower():
                print(
                    f"{expense['Date']} | "
                    f"{expense['Category']} | "
                    f"₹{expense['Amount']}"
                )
                found = True

        if not found:
            print("No Matching Expenses Found!")

    # Delete Expense
    elif choice == "5":
        if expenses:
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['Date']} | "
                    f"{expense['Category']} | "
                    f"₹{expense['Amount']}"
                )

            delete_index = int(input("Enter Expense Number to Delete: "))

            if 1 <= delete_index <= len(expenses):
                deleted = expenses.pop(delete_index - 1)
                save_data()

                print("Deleted:", deleted["Category"])
            else:
                print("Invalid Number!")

        else:
            print("No Expenses Found!")

    # Highest Expense
    elif choice == "6":
        if expenses:
            highest = max(expenses, key=lambda x: x["Amount"])

            print("\nHighest Expense")
            print(
                f"{highest['Date']} | "
                f"{highest['Category']} | "
                f"₹{highest['Amount']}"
            )
        else:
            print("No Expenses Found!")

    # Lowest Expense
    elif choice == "7":
        if expenses:
            lowest = min(expenses, key=lambda x: x["Amount"])

            print("\nLowest Expense")
            print(
                f"{lowest['Date']} | "
                f"{lowest['Category']} | "
                f"₹{lowest['Amount']}"
            )
        else:
            print("No Expenses Found!")

    # Monthly Summary
    elif choice == "8":
        summary = {}

        for expense in expenses:
            month = expense["Date"][:7]

            if month in summary:
                summary[month] += expense["Amount"]
            else:
                summary[month] = expense["Amount"]

        print("\n--- Monthly Summary ---")

        for month, total in summary.items():
            print(f"{month} : ₹{total}")

    # Exit
    elif choice == "9":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")
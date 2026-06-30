import json

def add_expenses():
    print("\n-------- Add Expense --------")

    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except:
        expenses = []

    # Add new expense to the list
    expenses.append(expense)

    # Save updated list
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("\nExpense Added Successfully!")

    print("\nExpense Details")
    print("Amount:", expense["amount"])
    print("Category:", expense["category"])
    print("Description:", expense["description"])

def view_expenses():
    print("View Expenses")

def delete_expense():
    print("delete expenses")

def display_menu():
    print("==============================")
    print("      Expense Tracker")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expenses")
    print("4. Monthly Summary")
    print("5. Category Summary")
    print("6. Exit")
    


display_menu()
    
#takes user input

choice = input("Enter your choice: ")
#print("You entered:", choice)


#decion making

if choice == "1":
    add_expenses()

elif choice == "2":
    view_expenses()

elif choice == "3":
    delete_expense()

elif choice == "4":
    print("Monthly Summary Selected")

elif choice == "5":
    print("Category Summary Selected")

elif choice == "6":
    print("Thank you for using Expense Tracker!")

else:
    print("Invalid Choice!")    


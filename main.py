# createing the function 

import json

def add_expense():
    print("\n--------Add Expenses--------")

    amount = float(input("Enter Amount: "))
    category = input("Enter Category:")
    description = input("Enter Description:")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    
    try:
        with open("expense.json","r") as file:  #opens file
            expenses = json.load(file)  

    except:
        expenses = []  #says start with an empty list        


    print("\nExpense Added Successfully")
    print("Amount:", expense["amount"])
    print("Category:", expense["category"])
    print("Description:", expense["description"])

def view_expenses():
    print("View Expenses")

def delete_expense():
    print("delete expense")

def display_menu():
    print("==============================")
    print("      Expense Tracker")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Summary")
    print("5. Category Summary")
    print("6. Exit")
    


display_menu()
    
#takes user input

choice = input("Enter your choice: ")
#print("You entered:", choice)


#decion making

if choice == "1":
    add_expense()

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


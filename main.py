# createing the function for displaying the menu

def add_expense():
    print("add expense")

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


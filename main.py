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
    

choice = input("Enter your choice: ")
print("You entered:", choice)

if choice == "1":
    print("Add Expense Selected")

elif choice == "3":
    print("View Expenses Selected")

elif choice == "3":
    print("Delete Expense Selected")

elif choice == "4":
    print("Monthly Summary Selected")

elif choice == "5":
    print("Category Summary Selected")

elif choice == "6":
    print("Thank you for using Expense Tracker!")

else:
    print("Invalid Choice!")    
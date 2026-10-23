expense = []

def add_expense():
    name = input("name of expense:- ")
    amount = float(input("amount od expense:- "))
    expense.append({"name" :name  , "amount" : amount})
    print("Expense saved successful....")

def view_expense():
    for i in expense:
        print(i ["name"] , ":-:",i ["amount"])

def total():
    total = 0
    for i in expense:
        total = total + i["amount"]
    print("total is:-  ", total)

print(" 1. Add 2. View 3 Total 4 Exit")
choice = input("Enter your choice:- ")

while choice != "4":

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3" :
        total()
    else :
        print("Invlid Choice")
    print(" 1. Add 2. View 3 Total 4 Exit")
    choice = input("Enter your choice:- ")


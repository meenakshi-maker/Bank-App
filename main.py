#------------------------------>>>>>>>>>>>>>>menu maker----------
def menuLoad(menu):
    count = 1

    for z in menu:
        print(f"{count}. {z}")


        count += 1

    print(f"0. EXIT")

    choice = input("Enter Number: ")

    if choice.isnumeric():

        choice = int(choice)

        if choice in range(0, count):

            answer = choice

        else:

            print("Error: Number out of RANGE.")

            answer = 99

    else:

        print("Error: Input NOT a number.")

        answer = 99

    return answer
#-----------------------------
def custFind():
    found = 0
    print("-------------FIND Customer-------")
    findMenu = ["by NAME", "by NUMBER"]
    selection = menuLoad(findMenu)

    if selection == 1:
        findFName = input("Enter FIRST Name: ").lower()
        findLName = input("Enter LAST Name: ").lower()

        for x in custList:
            if x.CustFName.lower() == findFName and x.CustLName.lower() == findLName:
                found = x
                print("Customer FOUND")
                break
    elif selection == 2:
        findNum = input("Enter Account Number: ")
        found = 0
        if findNum.isnumeric():
            findNum = int(findNum)

        for y in custList:
            if y.CustAcct.AccNum == findNum:
                found = y
                print("Customer FOUND")
                break
        else:
            print("Error")
    return found

def custEdit():
    fileEdit = custFind()

    if fileEdit != 0:
        editMenu = ["FIRST Name", "LAST Name", "EMAIL", "Account TYPE"]
        editPick = menuLoad(editMenu)

        if editPick == 1:
            fileEdit.setFName()
        elif editPick == 2:
            fileEdit.setLName()
        elif editPick == 3:
            fileEdit.setEmail()
        elif editPick == 4:
            fileEdit.CustAcct.setType()
        else:
            print("Error")


"""def findByNum():
    findNum = input("Enter Account Number: ")
    found = 0
    if findNum.isnumeric():
        findNum = int(findNum)

    for y in custList:
        if y.CustAcct.AccNum == findNum:
            found = y
            print("Customer FOUND")
            break
    else:
        print("Not a number")
        
    return found
"""
from Accounts import Account
from Customers import Customer

custList = []


dat01 = Customer(Account("Savings"), "Kylie", "Mackay")

dat02 = Customer(Account("Cheque"), "Donna", "Underwood")

dat03 = Customer(Account("Business"), "Anthony", "Hudson")
#custList.append(dat01) allow one at a time

custList.extend([dat01, dat02, dat03])

menu1 = ["DEPOSIT", "WITHDRAW", "Customer Menu"]
menu2 = ["FIND", "ADD", "EDIT", "Show All"]

while True:
    choice1 = menuLoad(menu1)

    if choice1 == 0:
        print("Goodbye")
        break

    elif choice1 == 1:
        depFind = custFind()

        if depFind != 0:
            print(f"Current Balance.{depFind.getCurrency()}")
            depAmt = input("ENTER DEPOSIT Amount: ")
            if depAmt.isnumeric():
                depAmt = float(depAmt)
                depFind.Deposit(depAmt)
                print(f"New Balance: {depFind.getCurrency()}")
            else:
                print("Not a Number")

    elif choice1 == 2:
       wdrFind = custFind()

       if wdrFind != 0:
           curBal = wdrFind.CustAcct.getBal()
           print(f"Current Balance.{curBal}")
           wdrAmt = input("ENTER WITHDRAWAL Amount: ")
           if wdrAmt.isnumeric():
               wdrAmt = float(wdrAmt)
               if wdrAmt > wdrFind.CustAcct.getBal() :
                   print("Insufficient Funds")
               else:
                   wdrFind.Withdraw(wdrAmt)
                   print(f"New Balance : {wdrFind.CustAcct.getBal()}")
           else:
               print("Not a Number")


    elif choice1 == 3:

        choice2 = menuLoad(menu2)

        if choice2 == 1:


            found = custFind()

            if found != 0:
                print(found)
            else:
                print("Customer NOT FOUND")

        elif choice2 == 2:
            print("Customer ADD")

        elif choice2 == 3:
            custEdit()

        elif choice2 == 4:
            for x in custList:
                print(x)
        else:
            continue




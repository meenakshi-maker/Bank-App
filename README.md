This code demonstrates a simple banking system where customers and their accounts are managed.
 Break down of the code
1. The code defines two classes: ‘Customer’ and ‘Account’, each in their respective files.
 2. The ‘Customer’ class represents a customer and has attributes like account (‘CustAcct’), first name (‘CustFName’), last name (‘CustLName’), and email (‘CustEmail’). It also has methods like ‘setFName()’, ‘getCurrency()’, ‘setLName()’, ‘setEmail()’,’Deposit()’, ‘Withdraw()’, and `__str__()` for modifying and retrieving customer information. 

3. The `Account` class represents a customer's bank account and has attributes like account number (‘AccNum’), account type (‘AccType’), and account balance (‘AccBal’). It also has methods like ‘getNum()’, ‘getType()’, ‘setType()’, and ‘getBal()’ for retrieving and modifying account information.
 4. The ‘menuLoad()’ function is a helper function that displays a menu and takes user input to select an option.
 5. The ’custFind()’ function allows users to find a customer either by name or account number and returns the found customer object.
 6. The ‘custEdit()’ function allows users to edit customer information like first name, last name, email, and account type.
 7. The code creates instances of `Account` and `Customer` classes and adds them to the ‘custLis’ list. 
8. The code uses a menu system to provide options like deposit, withdrawal, finding a customer, adding a customer, editing a customer, and showing all customers.
 9. Based on user input, the code performs the corresponding actions like depositing or withdrawing money, finding, and displaying customer information, adding a new customer, or editing existing customer information.

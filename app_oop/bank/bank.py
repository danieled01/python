#This is a small class that holds for methods which treats the account as the object we will be mapping to the class.

class account:

#The __init__ method initiates the class and creates a minimal product which results in the account.txt file being opened.  This will remain open until we close it right at the end. The close mothod needs to be explicitly called in order to write the new balance
    def __init__(self,location):
        self.location = location
        with open(location) as file:
            self.account = file.read()
#The self.account variable is broken up into self(object mapped to the class) and account(variable).  What happens here is that when we open the file for reading we map the contents of it to the obejct variable. 

#In both the withdraw and deposit methods we reference the self.account variable which gets mapped to the contents of the account.txt file after it gets opened for reading.  We then create a new self.account variable by adding/subtractinng the amounts passed as arguments to the withdraw/deposit methods.
    def withdraw(self, withdraw):
        self.account = int(self.account) - withdraw

    def deposit(self, deposit):
        self.account = int(self.account) + deposit

#The last method is the one that saves the file with the new amount for our bank account.  We open the file for writing and instead of passing the location of the file as a parameter to the method we grab it from the __init__ method as we previously mapped self.location = location.
    def save(self):
        with open(self.location, 'w') as file:
            file.write(str(self.account))

#In order to initialize the class we map an object to it with the parameter specified in the __init__ method.
acc=account('account.txt')

#After we initialize the method we can access the rest of the methods within it by using obejct name and passing the methods with the . notation and the parameters required for the methods to run.
acc.withdraw(200)
acc.deposit(500)
acc.save()

#inheritance is the concept of creating a parent class and then spawning off children classes off of it which can access the parent's methods.  This allows us to create a template to re-use when new use cases arise and thus removing code duplication.


#Parent/Base Class
class account:

    def __init__(self,location):
        self.location = location
        with open(location) as file:
            self.account = file.read()

    def withdraw(self, withdraw):
        self.account = int(self.account) - withdraw

    def deposit(self, deposit):
        self.account = int(self.account) + deposit

    def save(self):
        with open(self.location, 'w') as file:
            file.write(str(self.account))

#Child/Sub class
#we map the child class to the parent class by passing the name of the parent class as parameter to the child class - checking(account).
class checking(account):

#Our __init__ for the child class will reference the __init__ method of the parent class as that will create our minimal product whih in our case is opening the file and reading the balance - we do this via account.__init__ with the 2 parameters specified above.
    def __init__(self,location):
        account.__init__(self,location)

#you can also pass local variables into your child class and not just inheret from the parent class as per the example below where we declare a fee for our transfer.
    def transfer(self,amount,fee):
        self.account = self.account - amount - fee

#Below is how you call the methods from both classes via an object mapped to the child class - so check=checking('account.txt') maps the object check to the checking child class which has the same __init__ parameters as the parent class as they are required to initialise the minimal product.
check=checking('account.txt')

#We then call the deposit method in the parent class with its parameters - this is done via the object mapped to the class and method name.
check.deposit(200)

#Here we call the method declared in the child class with the paramaters required for transfer amount and fee.
check.transfer(500,200)

#We can also access the variables in the classes as we can access the account variable via the boject mapped to the class.
print(check.account)

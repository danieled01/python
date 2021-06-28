class base:

    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age

    def myname(self):
        print(self.name)

    def mysurname(self):
        print(self.surname)

    def myage(self):
        print(self.age)

dan=base("Homer","Simpson",39)
suzy=base("Marge","Simpson",37)

dan.myname()
suzy.mysurname()
dan.myage()
suzy.myage()

class mum(base):

    def __init__(self,name,surname,age):
        base.__init__(self,name,surname,age)

    def matleave(self,matleave):
        print(matleave)

suzy_mum=mum("Marge","Simpson",37)
suzy_mum.matleave("loving mat leave")

class dad(base):

    def __init__(self,name,surname,age):
        base.__init__(self,name,surname,age)

    def work(self,jobtitle):
        print(jobtitle)

dan_dad=dad("Homer","Simpson",39)
dan_dad.work("DEVOPS for the win")

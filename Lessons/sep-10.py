# OOP Object oriented programming
a = list()
a.append(12)
print(type(a))

b = int()
print(type(b))
# %%

class Oquvchi():
    ism = "O'quvchi"
    familiya = "Familiya"
    yosh = 15
    boy = 176.4
    erkakMi = True

o1 = Oquvchi()
print(o1.ism)
print(o1.familiya)
print(o1.yosh)
print(o1.boy)
print(o1.erkakMi)

# %%

class Mashina():
    def __init__(self,rang, model):
        print("men init methosiman !!!")
        self.m = model
        self.r = rang
    def otOl(self):
        print(f"{self.m} {self.r} -> Vinggg Vinggg")

m = Mashina("Sariq", "CHevrolet")
m.otOl()
# %%
class Employee():
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
    def showEmployee(self):
        print(f"Name: {self.name}")
        print(f"SurName: {self.surname}")
        print(f"Age: {self.age}")
        print(f"salary: {self.salary}")

ishchi1 = Employee("John", "Wick",23, 1400)
ishchi1.showEmployee()

ishchi2 = Employee("Bernard","Bear", 30, 1000)
ishchi2.showEmployee()
# %%
class Laptop():
    def __init__(self,model,ram,cpu,gpu,price):
        self.model = model
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self.price = price
    def showInfo(self):
        print(f"MOdel: {self.model}")
        print(f"Ram: {self.ram} GB")
        print(f"cpu: {self.cpu} GB")
        print(f"gpu: {self.gpu} GB")
        print(f"Price: {self.price}$")
    def changePrice(self,newPrice):
        self.price = newPrice
        
    def addSpesification(self,newSpesification):
        print(f"Qoshimcha qurilma: {newSpesification}")
        
acer = Laptop("Acer", 6, 5, 6, 1000)
acer.showInfo()
acer.addSpesification("mouse")        

acer = Laptop("Macbook", 8, 4, 8, 1200)
acer.showInfo()
# %%
class Developer():
    def __init__(self,name,surname,number,level,salary,langs):
        self.name = name
        self.surname = surname
        self.number = number
        self.level = level
        self.salary = salary
        self.languages = langs
    def showDeveloperInfo(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Number: {self.number}")
        print(f"Level: {self.level}")
        print(f"Salary: {self.salary}")
        print(f"Languages: {self.languages}")
    def changeLevel(self,newLang):
        self.level = newLang
    def salaryincres(self,count):
        self.salary += count
muzaffar = Developer("Muzaffar", "wick", 34, "Junior", 900, ["c","Python"])
muzaffar.showDeveloperInfo()
muzaffar.changeLevel("Middle")
muzaffar.salaryincres(100000)
muzaffar.showDeveloperInfo()
me = Developer(name, surname, number, level, salary, langs)

# %%
class Book():
    def __init__(self,name,page,author):
        self.name = name
        self.page = page
        self.author = author
    def __str__(self):
        return "Name: {} \nPage: {} \nAuthor: {}".format(self.name,self.page,self.author)
    def __len__(self):
        return self.page
    def __del__(self):
        print("Delete qilindi !!!")

kimyogar = Book("AL-Kimyogar",190, "Paolo Keolo")
print(kimyogar)

tomSoyer = Book(input("Name: "),int(input("Pages: ")),input("Author: "))
print(tomSoyer)
print(len(tomSoyer))

tomSoyer




































# class Student:
#     def introduce(self):
#         print("Welcome to OOP"
# #
# class Student:
#     pass
# stundent1 = Student()
# stundent1.name = "Mirbek"
# stundent1.age = 21
# stundent1.city = "Bishkek"
#
# stundent2 = Student()
# stundent2.name = "Aijan"
# stundent2.age = 24
# stundent2.city = "Osh"
#
# print(stundent1.name, stundent1.city)
# print(stundent2.name, stundent2.city,stundent2.age)



# class Student1:
#     pass
# stundent1 = Student1()
# stundent2 = Student1()
# print(stundent1)
# print(stundent2)

#
#
# def say_hello():
#     print("hello")
#
# say_hello()

# class Student:
#     def introduce(self):
#         print(f"my name is {self.name} ")
#         print(f"i'm an student {self.age}")
# student1 = Student()
# student1.name = "mirbek"
# student1.age = 20
#
# student2 = Student()
# student2.name = "Aijan"
# student2.age = 30
#
# student1.introduce()
# student2.introduce()

# _init_()


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"my name is {self.name}, my age is {self.age} ")
# student1 = Student("Mirbek", 17)
#
#
# student2 = Student(20, "Aijan")




# student1.introduce()
# student2.introduce()


# student1.introduce()
# student2.introduce()



# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def show_info(self):
#         print(f"Markasy: {self.brand}")
#         print(f"Modely: {self.model}")
#         print(f"chygarylgan jyly: {self.year}")
#     def start(self):
#         print(f"{self.brand} {self.model} satyuldy!")
#
# car1 = Car("Tayota","Camry",2022)
# car2 = Car("BMW","M5",2024)
#
# car1.show_info()
# car1.start()
#
# print('---------------')
#
# car2.show_info()
# # car2.start()



# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def show_balance(self):
#         print(f"name of owner: {self.owner}")
#         print(f"balance: {self.balance} som")
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} som koshuldu")
#
# account = BankAccount("Mirbek", 10000)
#
# account.show_balance()
# account.deposit(1000)
# account.show_balance()






# class BankAccount: _BankAccount__balance
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def show_balance(self):
#         print(f"name of owner: {self.owner}")
#         print(f"balance: {self.__balance} som")
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"deposited {amount} som")
#         else:
#             print(f"koshula turgan akcha on san bolushu kerek")
#
# account = BankAccount("Mirbek", 10000)
#
#
# account.show_balance()
# account.deposit(1000)
# account.deposit(-500)
# account.show_balance()



#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def show_balance(self):
#         print(f"name of owner: {self.owner}")
#         print(f"balance: {self.__balance} som")
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"deposited {amount} som")
#         else:
#             print(f"koshula turgan akcha on san bolushu kerek")
#
#     def chygary(self, amount):
#         if amount <= 0:
#             print("summa should be on san ")
#         elif amount > self.__balance:
#             print("akcha jetishsiz")
#         else:
#             self.__balance -= amount
#             print(f"chygaryldy {amount} som")
# account = BankAccount("Mirbek", 10000)
#
#
# account.show_balance()
# account.deposit(1000)
# account.chygary(900)
# account.chygary(10100)
# account.show_balance()
#
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self._email = "userexample@gmail.com"
#         self.__password = "qwertyuiop123456789"
#
#
# user = User("Ali")
#
# print(user.name)
# print(user._email)
# print(user.__password)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print(f"baasy on san bolushy kerek ")
#
# product = Product("Noutbuk",70000)
# print(product.price)
# product.price = 10000
# print(product.price)
# product.price = -10000
# print(product.price)
#




# 1. Student классы: __init__() аркылуу студенттин аты, жашы жана тобун кабыл алгыла.
# # show_info() методун түзүп, маалыматтарын чыгаргыла. Үч студенттин объектисин түзгүлө.
# class Student:
#     def __init__(self, name, age, toby):
#         self.name = name
#         self.age = age
#         self.toby = toby
#
#     def show_info(self):
#         print(f"Aty jonu : {self.name}")
#         print(f"jashy : {self.age}")
#         print(f"gruppasy : {self.toby}")
#
# student = Student("Saltanat",17,"NNN-2-25")
# student.show_info()
# # print(student.toby)

# 2. Car классы: Машинанын маркасы, түсү жана ылдамдыгы болсун. accelerate(amount) ылдамдыкты көбөйтсүн, brake(amount) ылдамдыкты азайтсын. Ылдамдык нөлдөн төмөн түшпөшү керек.
# 3. Rectangle классы: Туурасы жана бийиктиги берилсин. area() аянтын, perimeter() периметрин эсептесин. Туурасы жана бийиктиги оң сан болушу керек.
# 4. BankAccount классы: Ээсинин аты жана __balance балансы болсун. deposit(amount) акча кошсун, withdraw(amount) акча чыгарсын. Терс суммага жана баланстан көп акча чыгарууга уруксат бербегиле.
# 5. Product классы: Товардын аты жана __price баасы болсун. @property аркылуу бааны окугула, @price.setter аркылуу өзгөрткүлө. Баа нөлдөн жогору болушу керек.
# 6. LibraryBook классы: Китептин аталышы жана автору болсун. __is_borrowed атрибутун колдонгула. borrow() китеп бош болсо гана берилгенин белгилесин, return_book() китепти кайра жеткиликтүү кылсын. show_info() китептин учурдагы абалын чыгарсын.


# iheritance - muraskerlik - nasledie


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("janybar un chygarat")
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name}: muy-muy")
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name}: Af-Af!")
#
#
# cat = Cat("Myshyk")
# dog = Dog("It")
#
# cat.speak()
# dog.speak()


# class Person:
#     def __init__(self, name,age):
#         self.age = age
#         self.name = name
#     def introduce(self):
#         print(f"{self.name}: I am {self.age} years old")
#
#
# class Student(Person):
#     def study(self):
#         print(f"{self.name}: okup atat ")
#
# student = Student("James", 28)
#
#
# student.introduce()
# student.study()


# methodOverriding - metodty kayra anyktoo

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name}: janybar un chygarat")
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name}: muy-muy")
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name}: Af-Af!")
#
#
# animal = Animal("Kill")
# dog = Dog("wehrhru")
# cat = Cat("hisgh")
# animal.speak()
# dog.speak()
# cat.speak()
# cat = Cat("Myshyk")
# dog = Dog("It")
#
# cat.speak()
# dog.speak()



# class Vehicle():
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def show_info(self):
#         print(f"markasy: {self.brand}")
#         print(f"speed: {self.speed}")
#
# class Car(Vehicle):
#     def __init__(self, brand, speed, doors):
#         super().__init__(brand, speed)
#         self.doors = doors
#
#     def show_doors(self):
#         print(f"Eshikterdin sany: {self.doors}")
#
# class Motorsykle(Vehicle):
#     def __init__(self, brand, speed, had_sidecar):
#         super().__init__(brand, speed)
#         self.had_sidecar = had_sidecar
#
#     def show_had_sidecar(self):
#         print(f"prisep barby : {self.had_sidecar}")
#
#
# car = Car("Tayota", 180, 4)
# motorysykle = Motorsykle("Honda", 120, False)
# car.show_info()
# car.show_doors()
# print("--------------------")
# motorysykle.show_info()
# motorysykle.show_had_sidecar()


# hello()
#
# def hello():
#     print("salam")
#
# hello()
# hello()
# hello()

# name = "str"
# def hello():
#     print(name)
# hello()

# def add(name, age):
#     print(f"{name}, {age} added")
# add("Mirbek","20")
# add("NUrlan","30")

# def hello(a,b):
#     print(a + b)
# hello(5,10)

# def hello(name):
#     print(f"hello {name}!")
# name = input("what is your name? ")
# hello(name)
#
# hello() деген функция түзүп, "Hello Python" чыгар.
# def hello():
#     print("Hello Python")
# hello()
# welcome() деген функция түзүп, "Python курсуна кош келиңиз!" чыгар.
# def welcome():
#     print("Python курсуна кош келиңиз!")
# welcome()
# name() деген функция түзүп, өзүңдүн атыңды чыгар.
# def name():
#     print("Akylbek")
# name()
# numbers() деген функция түзүп, 1ден 10го чейинки сандарды for менен чыгар.
# def numbers():
#     for i in range(1,11):
#         print(i)
# numbers()
# even_numbers() деген функция түзүп, 1ден 20га чейинки жуп сандарды чыгар.
#     def even_numbers():
#         for i in range(1,21):
#             if i % 2 == 0:
#                 print(i)
#         name()
#     even_numbers()
# Функция түзүп, "Мен Python үйрөнүп жатам" деген текстти 3 жолу чыгар.
# def name():
#     name = "Мен Python үйрөнүп жатам"
#     for i in range(3):
#         print(name)
#
# name()
# name()
# name()

# def add(x,y):
#     if(x>y):
#         return x+y
#     elif(x<y):
#         print(x+y)
#     else:
#         return y*x
# rusult = add(3,4)
# fix = add(3,4)
#
#
# def check_age(age):
#     if age >= 18:
#         return "chon adam"
#     return "jashy jetelek adam"
# print(check_age(18))
#
# def chek_number(num):
#     if num > 0:
#         return "on san"
#     elif num < 0:
#         return "ters san"
#     else:
#         return "nol"
# print(chek_number(0))
# print(chek_number(1))
# print(chek_number(-2))

# Эки сан кабыл алган add() функциясын түз. Функция алардын суммасын return кылсын.
# def some_san(x, y):
#     return x + y
# print(some_san(2, 3))
# Эки сан кабыл алган multiply() функциясын түз. Функция алардын көбөйтүндүсүн return кылсын.
# square() функциясын түз. Бир сан кабыл алып, анын квадратын return кылсын.
# Эки сан кабыл алган max_number() функциясын түз. Чоң санды return кылсын.
# number_status() функциясын түз. Сан оң болсо "Оң сан", терс болсо "Терс сан", 0 болсо "Нөл" деген маанини return кылсын.
# is_even() функциясын түз. Сан жуп болсо True, так болсо False кайтарсын.
# get_full_name() функциясын түз. name жана surname кабыл алып, толук аты-жөнүн return кылсын.
# calculate_age() функциясын түз. Туулган жылды кабыл алып, адамдын жашын return кылсын.
# Үч сан кабыл алган average() функциясын түз. Үч сандын орточо маанисин return кылсын.
# Эки сан жана операция кабыл алган calculate() функциясын түз. Мисалы: calculate(10, 5, "+") → 15 calculate(10, 5, "-") → 5 calculate(10, 5, "*") → 50 calculate(10, 5, "/") → 2


# def add(name="mirbek"):  #Default - po umolchaniniyu
#     print(name)
# add(89)
#
# def aaaa(san=20):
#     print(san >= 20)
# aaaa(19)

# def numbr(num, age=20):
#     print(f'{num} is {age} years old')
# numbr("Mirbek", 19)

# def numbers(*args):
#     print(args)
# numbers(1,2,3,4,5,6,7,8,9,10)



# def numbers(*args):
#     return sum(args)
# print(numbers(1,2,3,4,5,6,7,8,9,10))
# print(numbers(9,10))
#
# def func(**kwargs): #key=value
#     print(kwargs)
# func(name="ali",age=19,city="bishkek",jym="everyday")
#
#
# def calculate(a,b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         return a / b
# print(calculate(1,2,"/"))
# print(calculate(1,2,"*"))
# print(calculate(1,2,"+"))
# print(calculate(1,2,"-"))


# hello() функциясын түз. name параметринин default мааниси "Student" болсун.
# def hello(name="Student"):
#     print(name)
# hello()
# introduce() функциясын түз. name милдеттүү, age default боюнча 18 болсун.
# def introduce(name,age=18):
#     print(name)
#     print(age)
# introduce("Mirbek",19)
# *args колдонуп, келген бардык сандардын суммасын эсептеген функция түз.
# def summa(*args):
#     return sum(args)
# print(summa(1,2,3,4,5,6,7,8,9))
# *args колдонуп, келген сандардын эң чоңун тап.
# def summa(*args):
#     return max(args)
# print(summa(1,2,3,4,5,6,7,10,9))
# # *args колдонуп, келген сандардын санын эсепте.
# def summa(*args):
#     return len(args)
# print(summa(1,2,3,4,5,6,7,10,9))
# **kwargs колдонуп, студенттин маалыматтарын кабыл алган функция түз.

# **kwargs аркылуу name, age, city маалыматтарын кабыл алып, экранга чыгар.
# *args колдонуп, бардык сандарды көбөйткөн функция түз.
# Бир функцияда name, age жана **kwargs колдонуп көр.




# def add1(a,b):
#     # return a+b
#         if a+b == 0:
#             print(True)
#         else:
#             print(False)

# add = lambda a, b: (
#     if a+b = 0:
#         print
# )

# print(add(8, 9))
# print(add1(8, 9))

# cheap = lambda x: "Jup" if x % 2 == 0 else "tak"
#
# print(cheap(1))

#
# numbers = [1",2,3,4,5,6,7,10,9"]
#
# result = list(map(lambda x: x * 2, numbers))
# def res(x):
#     numbers = (1, 2, 3, 4, 5, 6, 7, 10, 9)
#     for x in numbers:
#         x * 2
#         return x * 2
#
# print(res(1))

# map()
# filter()
#
# map()


# numbers = [1,2,3,4,5,6,7,10,9]
# result = list(map(lambda x: x ** 2, numbers))
# print(result)

# names = ["Mirbek", "Nurbek"]
# res = map(lambda name: name.upper(),names)
# print(list(res))


# numbers = [1, 2, 3, 4, 5] #Ар бир санды 3кө көбөйтүп, жаңы list түз.
# result = list(map(lambda x: x * 3, numbers))
# print(result)
# numbers = [1, 2, 3, 4, 5]. Ар бир сандын квадратын тап.
# numbers = [10, 20, 30, 40]. Ар бир сандан 5ти кемит.
# numbers = [1, 2, 3, 4, 5]. Ар бир санды string'ге айландыр.
# names = ["ali", "bek", "nursultan"]. Бардык аттарды баш тамга менен чыгар.
# words = ["python", "javascript", "typescript"]. Ар бир сөздүн узундугун тап.
# prices = [100, 200, 300, 400]. Ар бир баага 10% кош.
# ages = [15, 18, 20, 25]. Ар бир жашты 2ге көбөйт.
# numbers = [2, 4, 6, 8, 10]. Ар бир санды 2ге бөл.
# numbers = [1, 2, 3, 4, 5]. Ар бир санды "Жуп" же "Так" деген текстке айландыр.


# nums = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda x: x % 2 != 0, nums)
# print(list(result))
#
# nums = [1,2,3,4,5,6,7,8,9,10]
# result = map(lambda x: x % 2 != 0, nums)
# print(list(result))



# numbers = [25, 67, 5, 99, 87, 1000]
# chon_sandar = filter(lambda x: x > 50, numbers)
# print(list(chon_sandar))
#
# numbers = [25, 67, 5, 99, 87, 1000]
# chon_sandar = map(lambda x: x > 50, numbers)
# print(list(chon_sandar))


# names = ["MIrbek", "Nurik","Nargiza"]
# result = filter(lambda name: len(name) > 6, names)
# print(list(result))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]. Жуп сандарды filter() аркылуу тап.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]. Так сандарды filter() аркылуу тап.
# numbers = [5, 12, 3, 20, 15, 7]. 10дон чоң сандарды тап.
# numbers = [5, 12, 3, 20, 15, 7]
# chon_sandar = filter(lambda x: x > 10, numbers)
# print(list(chon_sandar))
# numbers = [5, 12, 3, 20, 15, 7]. 10дон кичине сандарды тап.
# numbers = [-5, 10, -3, 7, -1, 8]. Оң сандарды гана танда.
# numbers = [-5, 10, -3, 7, -1, 8]. Терс сандарды гана танда.
# ages = [12, 17, 18, 20, 15, 25]. 18 жаштан чоң же барабар болгон жаштарды тап.
# names = ["Ali", "Bek", "Azamat", "Aibek", "Nur"]. Узундугу 4төн чоң болгон аттарды тап.
# numbers = [10, 15, 20, 25, 30, 35]. 5ке бөлүнгөн сандарды filter() менен тап.
# numbers = [1, 2, 3, 4, 5]. Алгач filter() менен жуп сандарды тандап, андан кийин map() менен аларды 2ге көбөйт.
# nums = [1, 2, 3, 4, 5]
# result = filter(lambda x: x % 2 == 0, nums)
# result_x = map(lambda x: x * 2, result)
# print(list(result))
# # print(list(result_x))



# name = ["lmirbek", "Nurvek"]
# age = [77, 99]
# city = ["bishkek", "Osh"]
# result = zip(name, age, city)
# print(list(result))
#
# for names, ages, citys in zip(name, age,city):
#     print(names, ages, citys)

# result = dict(zip(name, age))
# print(result)

#
# student = ["ali", "nursultan", "aza", "nur"]
# baa = [5, 3, 4, 2]
#
# for students, baas in zip(student, baa):
#     if(baas >= 3):
#         print(students, baas)


#
# 1. names жана ages деген эки list түз. zip() жана for колдонуп,
# ар бир адамдын атын жана жашын чыгар.

# 2. products жана prices деген эки list түз. zip() жана for колдонуп, ар бир
# товарды баасы менен чыгар.
# products = ['Airan', 'cyt']
# prices = [10000, 5000]
# for product, price in zip(products, prices):
#     print(f"{product} -> {price} som")
# 3. students жана grades деген эки list түз. zip() колдонуп,
# студенттин атын жана баасын чыгар.
# 4. students жана grades list’терин zip() аркылуу бириктирип,
# баасы 4 же 5 болгон студенттерди гана чыгар.
# 5. names, ages, cities деген 3 list түз. zip() колдонуп, адамдын атын,
# жашын жана шаарын бирге чыгар.
# 6. keys = ["name", "age", "city"] жана values = ["Ali", 20, "Bishkek"]
# деген list түз. zip() жана dict() колдонуп dictionary түз.
# 7. names жана scores деген list түз. zip() жана dict() колдонуп,
# студенттердин аттарын ачкыч, баллдарын мааниси кылып dictionary түз.
# 8. numbers1 = [1, 2, 3] жана numbers2 = [10, 20, 30] деген эки
# list түз. zip() колдонуп, бирдей индекстеги сандардын суммасын чыгар.
# 9. names жана ages деген эки list түз. zip() менен бириктирип,
# list() аркылуу жаңы list түз.
# 10. products жана prices деген эки list түз. zip() жана dict()
# колдонуп dictionary түзүп, андан кийин for аркылуу ар бир товарды жана баасын чыгар.
# 11. names = ["Ali", "Bek", "Aza", "Mira"] жана ages = [17, 20, 18, 16]
# берилген. zip() + for + if колдонуп, 18 жаштан улуу адамдарды чыгар.
# 12. names = ["Ali", "Bek", "Aza"] жана scores = [80, 95, 70] берилген.
# zip() + if колдонуп, 80ден жогору балл алган студенттерди чыгар.
# 13. numbers1 = [1, 2, 3, 4, 5] жана numbers2 = [10, 20, 30, 40, 50]
# берилген. zip() колдонуп, эки сандын көбөйтүндүсүнөн жаңы list түз.
# 14. names жана salary деген эки list түз. zip() жана dict() колдонуп
# dictionary түз. Андан кийин айлыгы 50000 сомдон жогору болгон адамдарды чыгар.
# 15. names, ages, scores деген 3 list түз. zip() + for + if колдонуп,
# 18 жаштан улу у жана 80ден жогору балл алган студенттерди чыгар.



# list compreshion, dict compreshion

# numbers = [1, 2, 3, 4, 5]
# result = []
# for number in numbers:
#     result.append(number * 2)
# print(result)



# numbers = [1, 2, 3, 4, 5]
# result = [number * 2 for number in numbers  ]
# print(result)

# numbers = [20, 19, 18]
# names = ["Mirbek","Adilet","Mahmanazar"]
#
# result = {name: age for name, age in zip(names, numbers)}
# print(result)


# [expression for item in iterable]
# [expression for item in iterable if condition]

# {key: value for item in iterable}
#
# numbers = [1, 2, 3, 4, 5]
# result = [x for x in numbers if x.length % 2 == 0  ]
# print(result)




# 1. numbers = [1, 2, 3, 4, 5] берилген. List comprehension колдонуп, ар бир санды 2ге көбөйткөн жаңы list түз.
# 2. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] берилген. List comprehension колдонуп, жуп сандардан жаңы list түз.
# 3. numbers = [1, 2, 3, 4, 5] берилген. List comprehension колдонуп, ар бир сандын квадратын чыгар.
# 4. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] берилген. List comprehension колдонуп, 5тен чоң сандарды гана ал.
# 5. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] берилген. List comprehension колдонуп, 3кө бөлүнгөн сандарды гана ал.
# 6. names = ["Ali", "Bek", "Aza", "Mira"] берилген. List comprehension колдонуп, бардык аттарды uppercase кылып жаңы list түз.
# 7. names = ["Ali", "Bek", "Aza", "Mira"] берилген. List comprehension колдонуп, узундугу 4төн чоң болгон аттарды гана ал.
# 8. numbers = [1, 2, 3, 4, 5] берилген. lambda + map() колдонуп, ар бир санга 10 кош.
# 9. numbers = [1, 2, 3, 4, 5, 6] берилген. lambda + filter() колдонуп, жуп сандарды гана ал.
# 10. numbers = [1, 2, 3, 4, 5, 6] берилген. filter() менен жуп сандарды алып, андан кийин map() менен аларды 2ге көбөйт.
# 11. names = ["Ali", "Bek", "Aza"] жана ages = [18, 20, 19] берилген. zip() колдонуп, ат менен жашты бириктир.
# 12. names = ["Ali", "Bek", "Aza"] жана ages = [18, 20, 19] берилген. zip() + dict() колдонуп, төмөнкүдөй dictionary түз:
# {"Ali": 18, "Bek": 20, "Aza": 19}
# 13. names = ["Ali", "Bek", "Aza"] жана scores = [90, 65, 85] берилген. zip() + for + if колдонуп, 80ден жогору балл алган студенттерди чыгар.
# 14. names = ["Ali", "Bek", "Aza"] жана ages = [18, 20, 16] берилген. zip() колдонуп, 18 жаштан улуу же барабар студенттерди чыгар.
# 15. numbers = [1, 2, 3, 4, 5] берилген. List comprehension колдонуп, жуп сандарды 2ге көбөйтүп жаңы list түз.
# 16. numbers = [1, 2, 3, 4, 5, 6, 7, 8] берилген. List comprehension колдонуп, жуп сандардын квадраттарын гана чыгар.
# 17. names = ["Ali", "Bek", "Aza"] жана ages = [18, 20, 19] берилген. zip() + dict comprehension колдонуп dictionary түз.
# 18. names = ["Ali", "Bek", "Aza", "Mira"] жана scores = [90, 60, 85, 45] берилген. Dict comprehension колдонуп, 80ден жогору балл алган студенттерди dictionary катары чыгар.
# 19. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] берилген. filter() колдонуп жуп сандарды тап, андан кийин map() колдонуп квадратын чыгар.
# 20.  names = ["Ali", "Bek", "Aza", "Mira"], ages = [18, 21, 17, 20], scores = [90, 75, 95, 85] берилген. zip() колдонуп үч list’ти бириктир. Андан кийин if менен жашы 18ден жогору жана баллы 80ден жогору болгон студенттерди чыгар.
# Финалдык тапшырма
# 1. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] берилген.
# Бир эле программада:
# • filter() менен жуп сандарды ал;
# • map() менен аларды квадрат кыл;
# • List comprehension менен жыйынтыкты жаңы list кыл;
# • акырында экранга чыгар.

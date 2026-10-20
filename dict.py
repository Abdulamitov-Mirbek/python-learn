# student = {
#     'name': 'Mirbek',#name - keys : Mirbek - value
#     "age": 20
# }
#
# print(student['name'], ["age"]) Mirbek ['age']
# print(student['age'])

# numbers = [10, 20 , 39, 80, 90]
#
# print(numbers[4])

# student = {
#     'name': ['Mirbek', "Adilet"],
#     "age": 20,
#     "height": 80,
#     "weight": 70.9,
#     "num": True,
# }
# print(student["name"[1]])
# print(student["age"])
# print(student["height"])
#
# student = {
#     'name': ['Mirbek', "Adilet"],
#     "age": 20,
#     "height": 80,
#     "weight": 70.9,
#     "num": True,
# }
#
# print("name" in student)
# print("age" in student)
# print("heigh" in student)

# student["city"] = "bisshkek"
# student["name"] = "Mirbek"

# del student["weight"]
# print(len(student))
# print(student["city"])
# print(student["name"])


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
#
#
# student = {
#     "name":name,
#     "age":age
# }
#
# print(student)

# Өзүңөр жөнүндө Dictionary түзгүлө: name, age, city деген маалыматтар болсун.
# me = {
#     "name" : "Mirbek",
#     "age" : 20,
#     "student": True,
#     "city": "Bishkek"
# }
#
# print(me)

# Dictionaryден name жана age маанилерин экранга чыгаргыла.
# Dictionaryге жаңы "language" деген key кошуп, Python маанисин бергиле.
# age маанисин башка санга өзгөрткүлө.
# city деген элементти del аркылуу өчүргүлө.
# Dictionaryде канча элемент калганын len() аркылуу чыгаргыла.
# Колдонуучудан name жана age алып, аларды Dictionaryге сактагыла.
# Dictionaryде "name" деген key барбы же жокпу in аркылуу текшергиле.


#
# me = {
#      "name" : "Mirbek",
#      "age" : 20,
#      "student": True,
#      "city": "Bishkek"
# }
# # print(me.keys())
# print(me.values())
# print(me.items())
# print(me.get("name"))
# me.update({"age": 25})
# print(me)
# me.pop("city")
# print(me)
# me.popitem()
# print(me)
# me.clear()
# print(me)

# keys - kluchtorgo kaylylat
# values - maanilerine kayrylat
# items - kluchtorgo kaylylat || maanilerine kayrylat
# .get - aluu
# update - koshuu || ozgortuu
# pop() - belgiluu kluchtu ochurot
# popitem() - akyryrnan key:value ochurot
# clear() - tazaloo



# Бардык keyлерди чыгаргыла.
# Бардык valueларды чыгаргыла.
# key жана valueларды чогуу чыгаргыла.
# get() менен "name" маалыматтарын алгыла.
# Dictionaryге "phone" кошкула.
# "age" маанисин өзгөрткүлө.
# "city" элементин pop() менен өчүргүлө.
# Dictionaryде "name" барбы, текшергиле.






# students = {
#      "Mirbek": 85,
#      "Nur": 70,
#      "Marat": 92,
# }
# # for name, score in students.items():
#      if score >= 82:
#           print(name, score)

# if "Mirbek" in students:
#      print("Mirbek bar eken")
# else:
#      print("jok eken")


# for name, age in students.items():
#      if age >=  18:
#           print(name)


# for key in student:
#      print(key)


# for value in student.values():
#      print(value)

# for key in student.keys():
#      print(key)
#
# for key in student.items():
#      print(key)



# 1. Dictionary түзгүлө:
# students = {
# "name": "Aibek",
# "age": 20,
# "city": "Bishkek"
# }
# for key in students.keys():
#      print(key)
# for колдонуп бардык key лерди чыгаргыла.
# 2. Ошол эле Dictionaryнин бардык valueлерин values() аркылуу чыгаргыла.
# 3. items() колдонуп key жана valueлерди бирге чыгаргыла.
# 4. Сандардан турган Dictionary түзгүлө:
# {
# "a": 10,
# "b": 25,
# "c": 8,
# "d": 40
# }
# for + if колдонуп 20дан чоң сандарды гана чыгаргыла.
# 5. Студенттердин баалары берилген:
# {
# "Ali": 85,
# "Bek": 60,
# "Aibek": 95,
# "Nurbek": 70
# }
# 80ден жогору баа алган студенттерди чыгаргыла.
# 6. Товарлардын баалары берилген:
# {
# "apple": 50,
# "banana": 80,
# "orange": 120
# }
# 100дөн кымбат товарларды чыгаргыла.
# 7. Dictionary берилген:
# {
# "Python": 3,
# "JavaScript": 5,
# "C++": 2,
# "Java": 4
# }
# 2ден көп болгон маанилерди чыгаргыла.
# 8. Колдонуучудан 3 студенттин атын жана жашын алып, Dictionaryге сактагыла.
# Андан кийин for + if колдонуп 18 жаштан улуу студенттерди чыгаргыла.
#

dict = {
    "id":1,
    "name":"mirbek"

}
dict  ["city"] = "Bishkek"
print(dict)

dict.replace("mirbek","nurbek")
print(dict)




name = "mirbek"
print(name)
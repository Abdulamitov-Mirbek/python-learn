# from os import write
#
# open(),
# read(),
# readline()
# readlines()
# write()
# w
# a
# with open()
#

# file = open("student.txt", "r")
# print(file.readline())


# file = open("student.txt", "r")
# line = file.readline()
# print(file.readline())
# file.close()
# file = open("student.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()
# for lineses in lines:
#     print(lineses.strip())

# strip()

# name = "ali\n"
#
# print(name.strip())



# file = open("student.txt", "w")
# file.write("Adilet\n")
# file.write("Nurbek\n")
# file.write("Mirbek\n")
# # file.close()
# print(file)
# file.close()

# file = open("student.txt", "a")
# file.write("\nhello world")
# file.write("\nHi")
# file.close()

# with open("student.txt","r") as file:
#     text = file.read()
# print(text)
# with open("student.txt","w") as f:
#     f.write("\nhello world")

# with open("student.txt","a") as f:
#     f.write("\nhello world2")

# count = 0
# with open("student.txt", "r") as f:
#     for line in f:
#         word = line.strip()
#
#         if word == "hello world":
#             count += 1
# print(count)


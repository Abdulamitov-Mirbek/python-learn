# csv -
# json
# import csv
import json
# with open("csv/csv.csv", "w", newline = "",encoding = "utf-8" ) as csvfile:
#     writer = csv.writer(csvfile)
#
#     writer.writerow(["name", "age", "grade"])
#     writer.writerow(["Ali", 18, 90])
#     writer.writerow(["Bek", 19, 80])
#     writer.writerow(["Aizada", 18, 95])
#
#
# student = [
#     ["name", "age", "grade"],
#     ["Ali", 18, 90],
#     ["Bek", 19, 80],
#     ["Aizada", 18, 95]
# ]
#
# with open("csv/student.csv", "w", newline = "",encoding = "utf-8" ) as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(student)


# json - javascript object notation
# true

# student = {
#   "name": "Ali",
#   "age": 18,
#   "grades": 90,
#   "is_student": True
# }
# with open("csv/student.json", "w", encoding="utf=8") as f:
#     json.dump(student, f, ensure_ascii=False, indent=4)

#
# student = {
#   "name": "bek",
#   "age": 25,
#   "grades": 80,
#   "is_student": False
# }
# with open("csv/student.json", "w", encoding="utf=8") as f:
# #     json.dump(student, f, ensure_ascii=False, indent=4)
#
# with open("csv/student.json", "r", encoding="utf=8") as f:
#     student = json.load(f)
#
# print(student)
# print(student["name"])
# print(student["age"])
# print(student["grades"])


# with open("csv/student.json", "r", encoding="utf-8") as f:
#     student = json.load(f)
# student["grades"] = 100
# with open("csv/student.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False, indent=4)

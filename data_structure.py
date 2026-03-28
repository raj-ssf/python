# Print the sum of all numbers in the list and find it's average.

# num = [1, 2, 3, 4, 5]
# sum = 0

# for n in num:
#     sum = sum + n
# print(sum)

# names = ["John", "David", "Michael", "Bob", "Paul", "Raj"]

# snames = sorted(names)

# for i, name in enumerate(snames):
#     print(f"{i}: {name}")

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = []
# for num in nums:
#     if num % 2 == 0:
#         evens.append(num)
# print(evens)

# evens = [num for num in nums if num % 2 == 0]
# print(evens)   # [2, 4, 6, 8, 10]



# person = {"name": "Alice", "age": 28, "city": "London"}

# for key, value in person.items():
#     print(f"{key}: {value}")


# student = {
#     "name": "Alice",
#     "grades": [92, 85, 96, 88],
#     "address": {
#         "street": "123 Main St",
#         "city": "London"
#     }
# }

# print(student["address"]["street"])

# employees = [
#     {"name": "Alice", "role": "QA", "salary": 80000},
#     {"name": "Bob", "role": "Developer", "salary": 95000},
#     {"name": "Charlie", "role": "Designer", "salary": 75000},
# ]

# devs = [emp for emp in employees if emp["role"] == "Developer"]
# print(devs)

# total = sum(emp["salary"] for emp in employees)
# print(total)


# new_dict = {"Title" : "Matrix", "Director" : "Wachowski", "Year" : 1999, "Rating" : "Excellent"}

# for key, value in new_dict.items():
#     print(f"{key}: {value}")



# string = "Mississippi"
# counts = {}

# for char in string:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1
# print(counts)
        



students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 78},
    {"name": "Charlie", "grade": 95},
    {"name": "David", "grade": 61},
    {"name": "Eve", "grade": 88},
]

grades = [ student for student in students if student["grade"] > 85 ]
print(grades)















































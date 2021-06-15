'''

dictionary

# students = ['Magy', 'Rashida', 'Muthoni', 'Raphael']
# for student in students:
#     print(student)

students = {
    "Name": "Sam",
    "Age": 19,
    "Gender": "M"
}

students["Name"] = "Tomashi"
print(students["Age"])

'''


students = [
    {
    "Name": "Rashida",
    "Age": 19,
    "Gender": "M"
    },
    {
        "Name": "Muthoni",
        "Age": 10,
        "Gender": "F"
    },
    {
        "Name": "Magy",
        "Age": 20,
        "Gender": "F"
    }
]


for student in students:
    print(student["Gender"])

for student in students:
    if student["Name"] == "Rashida":
        print(student["Name"])
        print(student["Age"])
        print(student["Gender"])
        
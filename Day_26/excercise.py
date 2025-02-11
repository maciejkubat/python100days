import pandas
student_dict = {'Alexandra': 55, 'Catherine': 31, 'Elizabeth': 53, 'James': 34, 'Jennifer': 4, 'John': 83, 'Luke': 74, 'Mark': 24, 'Paul': 75, 'Samantha': 96}

students_scores = {
    "student": list(student_dict.keys()),
    "score": list(student_dict.values())
}

print(students_scores)

student_data_frame = pandas.DataFrame(students_scores)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.score)
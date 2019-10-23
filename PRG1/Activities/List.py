student_names = ["A", "B", "C"]
student_marks = [70, 80, 100]
student_dob = [1, 6, 10]

# for i in range(len(student_names)):
    # print(student_names[i], student_marks[i])

for name, mark, dob in zip(student_names, student_marks, student_dob):
    print(name, mark, dob)
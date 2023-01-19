students = int(input())
names_and_grades = {}

for student in range(students):
    name, grade = tuple(input().split())
    if name not in names_and_grades:
        names_and_grades[name] = [float(grade)]
    else:
        names_and_grades[name].append(float(grade))
for student, grades in names_and_grades.items():
    each_grade = ' '.join(map((lambda grade: f'{grade:.2f}'), grades)) # for each grade, turn it into a string, pass in the grades list
    print(f"{student} -> {each_grade} (avg: {sum(grades) / len(grades):.2f})")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    student_1 = Student("kunal", 25)
    student_2 = Student("Rahul", 22)
    list_of_student = list()
    list_of_student.append(student_1)
    list_of_student.append(student_2)
    for item in list_of_student:
        print(item.name)
        print(item.age)

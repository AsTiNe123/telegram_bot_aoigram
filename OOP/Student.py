
class Student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
        
        
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    
class HomelessStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.status = 'homless'

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, status: {self.status}"

def f():
    student1 = Student('Dima', '16')
    student2 = Student('Alexey', '15')
    student3 = HomelessStudent('fgah', '25')
    print(student1)
    print(student2)
    print(student3, f"count: {student3.count}")

f()
f()
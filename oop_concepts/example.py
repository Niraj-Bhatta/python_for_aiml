class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

student1 = Student("Ram", 85)
student2 = Student("Sita", 72)

student1.display()
print("---")
student2.display()
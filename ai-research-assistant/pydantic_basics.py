from pydantic import BaseModel
class Student(BaseModel):
    name: str
    age: int
    cgpa: float

student = Student(
    name="John",
    age=20,
    cgpa=3.5
)

print(student.name)
print(student.age)
print(student.cgpa)
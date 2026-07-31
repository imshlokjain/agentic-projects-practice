from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field(
        description="City name",
        min_length=2,
        max_length=30
    )

    country: str = Field(
        description="Country name",
        min_length=2,
        max_length=30
    )


class Student(BaseModel):
    name: str = Field(
        description="Student's full name",
        min_length=3,
        max_length=30
    )

    age: int = Field(
        description="Student's age",
        gt=0,
        lt=120
    )

    cgpa: float = Field(
        description="Student's CGPA",
        ge=0,
        le=10
    )

    address: Address


class Course(BaseModel):
    name: str = Field(
        description="Name of the course"
    )

    students: list[Student] = Field(
        description="Students enrolled in the course"
    )


course = Course(
    name="Artificial Intelligence",
    students=[
        {
            "name": "John",
            "age": 20,
            "cgpa": 8.5,
            "address": {
                "city": "New York",
                "country": "USA"
            }
        },
        {
            "name": "Alice",
            "age": 21,
            "cgpa": 9.1,
            "address": {
                "city": "London",
                "country": "UK"
            }
        }
    ]
)


for student in course.students:
    print(student.name)
    print(student.age)
    print(student.cgpa)
    print(student.address.city)
    print(student.address.country)
    print()
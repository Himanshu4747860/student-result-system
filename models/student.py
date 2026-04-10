from pydantic import BaseModel

class student(BaseModel):
    student_name: str
    student_rollno: int
    student_class: int

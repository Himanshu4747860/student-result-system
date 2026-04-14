from pydantic import BaseModel

class student(BaseModel):
    name: str
    rollno: int
    student_class: int
    english_mark: int
    hindi_mark: int
    science_mark: int
    maths_mark: int
    sst_mark: int
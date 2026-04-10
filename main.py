from fastapi import FastAPI
from models.marks import marks
from models.student import student
from services.calculator import result

app = FastAPI()

@app.post('/student')
def add_student(student: student):
    return {
        "message": "Student added successfully",
        "data": student
    }

@app.post('/add_marks')
def add_marks(marks: marks):
    return{ "message": f"{marks} this is your marks"}

@app.post('/show_result')
def show_result(result: result):
    return{"total":result.total,
           "percentage":result.percentage
            }

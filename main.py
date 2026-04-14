from fastapi import FastAPI, Form
from models.student import student
from services.calculator import result


app = FastAPI()

@app.post("/student")
def add_student(
    name: str = Form(...),
    rollno: int = Form(...),
    student_class: int = Form(...),
    english_mark: int = Form(...),
    hindi_mark: int = Form(...),
    science_mark: int = Form(...),
    maths_mark: int = Form(...),
    sst_mark: int = Form(...)
):
    return {
        "message": "Student added successfully",
        "data": {
            "name": name,
            "rollno": rollno,
            "student_class": student_class,
            "english_mark": english_mark,
            "hindi_mark": hindi_mark,
            "science_mark": science_mark,
            "maths_mark": maths_mark,
            "sst_mark": sst_mark
        },
        "student_info": f"{name} (Roll {rollno}) scored marks in class {student_class}"
    }


@app.post('/show_result')
def show_result(
    name: str = Form(...),
    rollno: int = Form(...),
    student_class: int = Form(...),
    english_mark: int = Form(...),
    hindi_mark: int = Form(...),
    science_mark: int = Form(...),
    maths_mark: int = Form(...),
    sst_mark: int = Form(...)
):
    student_data = student(
        name=name,
        rollno=rollno,
        student_class=student_class,
        english_mark=english_mark,
        hindi_mark=hindi_mark,
        science_mark=science_mark,
        maths_mark=maths_mark,
        sst_mark=sst_mark
    )
    result_obj = result(
        name=name,
        rollno=rollno,
        student_class=student_class,
        english_mark=english_mark,
        hindi_mark=hindi_mark,
        science_mark=science_mark,
        maths_mark=maths_mark,
        sst_mark=sst_mark
    )
    return {"total": result_obj.total, "percentage": result_obj.percentage}

from fastapi import FastAPI, Path
from typing import Optional
from src.services.services import get_all_students_service, get_student_by_id_service, get_student_by_name_service, create_student_service, delete_student_service, update_student_service
from src.models.student import Student

app = FastAPI()

@app.get('/get_all_students')
def getAllStudents():
    return get_all_students_service()

@app.get('/get_student_by_id/{student_id}')
def getStudentById(student_id: int = Path(description="The ID of the student you want to view")):
    return get_student_by_id_service(student_id)

@app.get('/get_student_by_name')
def getStudentByName(name: Optional[str] = None):
    return get_student_by_name_service(name)

@app.post('/create_student/{new_student_id}')
def createStudent(student_id: int, student: Student):
    return create_student_service(student_id, student)

@app.delete('/delete_student/{student_id}')
def deleteStudent(student_id: int):
    return delete_student_service(student_id)
    
@app.put('/update_student/{student_id}')
def updateStudent(student_id: int, name:Optional[str] = None, age: Optional[int] = None):
    return update_student_service(student_id, name, age)

from ..utils.utils import getAllStudents_utils, getStudentById_utils, getStudentByName_utils, createStudent_utils, deleteStudent_utils, updateStudent_utils

def get_all_students_service():
    return getAllStudents_utils()

def get_student_by_id_service(id):
    return getStudentById_utils(id)

def get_student_by_name_service(name):
    return getStudentByName_utils(name)

def create_student_service(student_id, student):
    return createStudent_utils(student_id, student)

def delete_student_service(student_id):
    return deleteStudent_utils(student_id)

def update_student_service(student_id, name, age):
    return updateStudent_utils(student_id, name, age)


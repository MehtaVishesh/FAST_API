students = {
    1: {"name": "Vishesh",
        "age":21
    },
    2: {"name": "Aanya",
        "age":13
    },
    3: {"name": "Aryan",
        "age":21
    },
    4: {"name": "Muktesh",
        "age":21
    }
}

def getAllStudents_utils():
    return students

def getStudentById_utils(student_id):
    return students[student_id]

def getStudentByName_utils(name):
    for studId in students:
        if students[studId]['name'] == name:
            return students[studId]
    return "Data not found"

def createStudent_utils(student_id, student):
    if student_id in students:
        return "Error, student already exists"
    
    students[student_id] = student
    return students[student_id]

def deleteStudent_utils(student_id):
    if student_id in students:
        del students[student_id]
    else:
        return "Error, student doesn't exist"

def updateStudent_utils(student_id, name, age):
    if name:
        students[student_id]["name"] = name
        return {f"Name changed to {name}"}
    if age:
        students[student_id]["age"] = age
        return {f"Age changed to {age}"}
    else:
        return "Nothing was updated"
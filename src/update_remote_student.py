
def update_remote_student(students):
    updated_students = students.copy()
    for student in updated_students:
        if 'location' not in student:
            student['location']='remote'
    return updated_students
    pass
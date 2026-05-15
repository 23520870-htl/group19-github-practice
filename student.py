students = []

def add_student(name, student_id):
    student = {
        "name": name,
        "id": student_id
    }
    students.append(student)

def show_students():
    if len(students) == 0:
        print("Danh sách trống")
    else:
        for student in students:
            print(f"Tên: {student['name']} - MSSV: {student['id']}")

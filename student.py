students = []
# Ham them sinh vien moi
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

# File quan ly sinh vien

def search_student(student_id):
    # Hàm tìm kiếm sinh viên theo MSSV
    for student in students:
        if student['id'] == student_id:
            return student
    return None

from student import add_student, show_students
from utils import search_student

while True:
    print("\n===== QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị sinh viên")
    print("3. Tìm kiếm sinh viên")
    print("4. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        name = input("Nhập tên: ")
        student_id = input("Nhập MSSV: ")
        add_student(name, student_id)

    elif choice == "2":
        show_students()

    elif choice == "3":
        keyword = input("Nhập tên cần tìm: ")
        search_student(keyword)

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")

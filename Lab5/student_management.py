
import unittest
from io import StringIO
import sys

class StudentManagement:
    """Lớp quản lý sinh viên"""
    
    def __init__(self):
        """Khởi tạo hệ thống"""
        self.students = [
            {
                "id": "SV001",
                "name": "Nguyễn Văn A",
                "email": "nguyenvana@student.edu.vn",
                "phone": "0912345678",
                "gpa": 3.8,
                "status": "Đang học"
            },
            {
                "id": "SV002",
                "name": "Trần Thị B",
                "email": "tranthib@student.edu.vn",
                "phone": "0987654321",
                "gpa": 3.5,
                "status": "Đang học"
            },
            {
                "id": "SV003",
                "name": "Lê Văn C",
                "email": "levanc@student.edu.vn",
                "phone": "0923456789",
                "gpa": 3.2,
                "status": "Đang học"
            }
        ]

    def show_students(self):
        """Hiển thị danh sách sinh viên"""
        if not self.students:
            print("Không có sinh viên nào trong hệ thống!")
            return False

        print("\n" + "="*100)
        print("DANH SÁCH SINH VIÊN CỦA HỆ THỐNG QUẢN LÝ")
        print("="*100)
        print(f"{'ID':<8} {'Tên Sinh Viên':<20} {'Email':<30} {'Điện thoại':<15} {'GPA':<8} {'Trạng thái':<15}")
        print("-"*100)
        
        for student in self.students:
            print(f"{student['id']:<8} {student['name']:<20} {student['email']:<30} {student['phone']:<15} {student['gpa']:<8} {student['status']:<15}")
        
        print("="*100)
        print(f" Tổng số sinh viên: {len(self.students)}")
        print("="*100 + "\n")
        return True

    def get_total_students(self):
        """Lấy tổng số sinh viên"""
        return len(self.students)

    def add_student(self, student_data):
        """Thêm sinh viên mới"""
        self.students.append(student_data)
        return True

    def get_students(self):
        """Lấy danh sách sinh viên"""
        return self.students

    def search_student_by_id(self, student_id):
        """Tìm sinh viên theo ID"""
        for student in self.students:
            if student['id'] == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        """Tìm sinh viên theo tên"""
        results = [s for s in self.students if name.lower() in s['name'].lower()]
        return results

    def get_students_by_status(self, status):
        """Lấy sinh viên theo trạng thái"""
        return [s for s in self.students if s['status'] == status]

    def get_students_by_gpa(self, min_gpa):
        """Lấy sinh viên có GPA >= min_gpa"""
        return [s for s in self.students if s['gpa'] >= min_gpa]


# ============================================================
# TEST CASES
# ============================================================

class TestShowStudents(unittest.TestCase):
    """Test cases cho hàm show_students()"""

    def setUp(self):
        """Chuẩn bị dữ liệu trước mỗi test"""
        self.system = StudentManagement()

    def tearDown(self):
        """Dọn dẹp sau mỗi test"""
        self.system = None

    # 1. Test hiển thị danh sách sinh viên
    def test_show_students_success(self):
        """Test hiển thị danh sách sinh viên thành công"""
        result = self.system.show_students()
        self.assertTrue(result, "Hàm show_students() phải trả về True")

    def test_show_students_empty(self):
        """Test hiển thị khi không có sinh viên"""
        empty_system = StudentManagement()
        empty_system.students = []
        result = empty_system.show_students()
        self.assertFalse(result, "Phải trả về False khi không có sinh viên")

    # 2. Test tổng số sinh viên
    def test_total_students(self):
        """Test đếm tổng số sinh viên"""
        total = self.system.get_total_students()
        self.assertEqual(total, 3, "Phải có 3 sinh viên")

    def test_add_student(self):
        """Test thêm sinh viên mới"""
        new_student = {
            "id": "SV004",
            "name": "Phạm Thị D",
            "email": "phamthid@student.edu.vn",
            "phone": "0934567890",
            "gpa": 3.9,
            "status": "Đang học"
        }
        self.system.add_student(new_student)
        self.assertEqual(self.system.get_total_students(), 4, "Phải có 4 sinh viên sau khi thêm")

    # 3. Test tìm kiếm sinh viên
    def test_search_by_id(self):
        """Test tìm sinh viên theo ID"""
        student = self.system.search_student_by_id("SV001")
        self.assertIsNotNone(student, "Phải tìm thấy sinh viên SV001")
        self.assertEqual(student['name'], "Nguyễn Văn A")

    def test_search_by_id_not_found(self):
        """Test tìm sinh viên theo ID không tồn tại"""
        student = self.system.search_student_by_id("SV999")
        self.assertIsNone(student, "Không phải tìm thấy sinh viên SV999")

    def test_search_by_name(self):
        """Test tìm sinh viên theo tên"""
        results = self.system.search_student_by_name("Nguyễn")
        self.assertEqual(len(results), 1, "Phải tìm thấy 1 sinh viên với tên Nguyễn")

    def test_search_by_name_case_insensitive(self):
        """Test tìm kiếm không phân biệt hoa/thường"""
        results = self.system.search_student_by_name("nguyễn")
        self.assertEqual(len(results), 1, "Tìm kiếm phải không phân biệt hoa/thường")

    # 4. Test lọc theo trạng thái
    def test_get_by_status(self):
        """Test lọc sinh viên theo trạng thái"""
        students = self.system.get_students_by_status("Đang học")
        self.assertEqual(len(students), 3, "Phải có 3 sinh viên đang học")

    def test_get_by_status_not_found(self):
        """Test lọc theo trạng thái không tồn tại"""
        students = self.system.get_students_by_status("Tốt nghiệp")
        self.assertEqual(len(students), 0, "Không phải tìm thấy sinh viên tốt nghiệp")

    # 5. Test lọc theo GPA
    def test_get_by_gpa(self):
        """Test lọc sinh viên có GPA >= 3.5"""
        students = self.system.get_students_by_gpa(3.5)
        self.assertEqual(len(students), 2, "Phải có 2 sinh viên có GPA >= 3.5")

    def test_get_by_gpa_threshold(self):
        """Test lọc sinh viên có GPA >= 4.0"""
        students = self.system.get_students_by_gpa(4.0)
        self.assertEqual(len(students), 0, "Không phải có sinh viên nào có GPA >= 4.0")

    # 6. Test dữ liệu sinh viên
    def test_student_data_structure(self):
        """Test cấu trúc dữ liệu sinh viên"""
        student = self.system.get_students()[0]
        required_fields = ['id', 'name', 'email', 'phone', 'gpa', 'status']
        
        for field in required_fields:
            self.assertIn(field, student, f"Sinh viên phải có field '{field}'")

    def test_student_id_unique(self):
        """Test ID sinh viên phải duy nhất"""
        ids = [s['id'] for s in self.system.get_students()]
        self.assertEqual(len(ids), len(set(ids)), "ID sinh viên phải duy nhất")

    def test_student_email_format(self):
        """Test định dạng email sinh viên"""
        for student in self.system.get_students():
            self.assertIn('@', student['email'], "Email phải chứa @")

    def test_student_phone_format(self):
        """Test số điện thoại phải là số"""
        for student in self.system.get_students():
            self.assertTrue(student['phone'].isdigit(), "Số điện thoại phải là số")

    def test_student_gpa_valid(self):
        """Test GPA phải trong khoảng 0-4.0"""
        for student in self.system.get_students():
            self.assertGreaterEqual(student['gpa'], 0, "GPA phải >= 0")
            self.assertLessEqual(student['gpa'], 4.0, "GPA phải <= 4.0")


# ============================================================
# TEST RUNNER
# ============================================================

if __name__ == '__main__':
    # Chạy tất cả test cases
    print("\n" + "="*70)
    print("CHẠY CÁC TEST CASE - CHỨC NĂNG HIỂN THỊ SINH VIÊN")
    print("="*70 + "\n")
    
    # Tạo test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestShowStudents)
    
    # Chạy tests với verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Tóm tắt kết quả
    print("\n" + "="*70)
    print("TÓM TẮT KẾT QUẢ TEST")
    print("="*70)
    print(f"Tổng tests: {result.testsRun}")
    print(f"Thành công: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Thất bại: {len(result.failures)}")
    print(f"Lỗi: {len(result.errors)}")
    print("="*70 + "\n")
    
    # Exit code
    exit(0 if result.wasSuccessful() else 1)
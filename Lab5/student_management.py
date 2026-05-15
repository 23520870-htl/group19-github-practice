"""
Hệ thống quản lý sinh viên - Student Management System
Chức năng: Hiển thị danh sách sinh viên (Member 3)
"""

class StudentManagement:
    def __init__(self):
        """Khởi tạo hệ thống quản lý sinh viên"""
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
            },
            {
                "id": "SV004",
                "name": "Phạm Thị D",
                "email": "phamthid@student.edu.vn",
                "phone": "0934567890",
                "gpa": 3.9,
                "status": "Đang học"
            }
        ]

    def show_students(self):
        """
        Hiển thị danh sách tất cả sinh viên
        Định dạng: Bảng thông tin chi tiết
        """
        if not self.students:
            print(" Không có sinh viên nào trong hệ thống!")
            return

        print("\n" + "="*100)
        print(" DANH SÁCH SINH VIÊN CỦA HỆ THỐNG QUẢN LÝ")
        print("="*100)
        
        # Tiêu đề bảng
        print(f"{'ID':<8} {'Tên Sinh Viên':<20} {'Email':<30} {'Điện thoại':<15} {'GPA':<8} {'Trạng thái':<15}")
        print("-"*100)
        
        # Hiển thị từng sinh viên
        for student in self.students:
            print(f"{student['id']:<8} {student['name']:<20} {student['email']:<30} {student['phone']:<15} {student['gpa']:<8} {student['status']:<15}")
        
        print("="*100)
        print(f" Tổng số sinh viên: {len(self.students)}")
        print("="*100 + "\n")

    def show_students_detailed(self):
        """
        Hiển thị danh sách sinh viên với thông tin chi tiết
        Định dạng: Danh sách chi tiết (dễ đọc hơn)
        """
        if not self.students:
            print(" Không có sinh viên nào trong hệ thống!")
            return

        print("\n" + "="*60)
        print(" THÔNG TIN CHI TIẾT SINH VIÊN")
        print("="*60)
        
        for index, student in enumerate(self.students, 1):
            print(f"\n{index}. Mã sinh viên: {student['id']}")
            print(f"   Tên: {student['name']}")
            print(f"   Email: {student['email']}")
            print(f"   Số điện thoại: {student['phone']}")
            print(f"   GPA: {student['gpa']}")
            print(f"   Trạng thái: {student['status']}")
            print("-"*60)
        
        print(f"\n Tổng cộng: {len(self.students)} sinh viên\n")

    def show_students_by_status(self, status):
        """
        Hiển thị sinh viên theo trạng thái
        Args:
            status: Trạng thái cần lọc (ví dụ: "Đang học", "Tốt nghiệp")
        """
        filtered_students = [s for s in self.students if s['status'] == status]
        
        if not filtered_students:
            print(f" Không tìm thấy sinh viên với trạng thái '{status}'")
            return

        print(f"\n{'='*80}")
        print(f" DANH SÁCH SINH VIÊN - TRẠNG THÁI: {status.upper()}")
        print(f"{'='*80}")
        print(f"{'ID':<8} {'Tên':<25} {'Email':<30} {'GPA':<8}")
        print("-"*80)
        
        for student in filtered_students:
            print(f"{student['id']:<8} {student['name']:<25} {student['email']:<30} {student['gpa']:<8}")
        
        print(f"{'='*80}")
        print(f" Tổng số: {len(filtered_students)} sinh viên\n")

    def show_top_students(self, limit=3):
        """
        Hiển thị các sinh viên có GPA cao nhất
        Args:
            limit: Số lượng sinh viên hiển thị (mặc định: 3)
        """
        sorted_students = sorted(self.students, key=lambda x: x['gpa'], reverse=True)
        top_students = sorted_students[:limit]

        print(f"\n{'='*70}")
        print(f" TOP {limit} SINH VIÊN CÓ GPA CAO NHẤT")
        print(f"{'='*70}")
        print(f"{'Xếp hạng':<12} {'Tên':<25} {'GPA':<10} {'Email':<25}")
        print("-"*70)
        
        for rank, student in enumerate(top_students, 1):
            print(f"{rank:<12} {student['name']:<25} {student['gpa']:<10} {student['email']:<25}")
        
        print(f"{'='*70}\n")

    def search_student(self, keyword):
        """
        Tìm kiếm sinh viên theo ID hoặc tên
        Args:
            keyword: Từ khóa tìm kiếm
        """
        results = [s for s in self.students if keyword.lower() in s['id'].lower() or keyword.lower() in s['name'].lower()]
        
        if not results:
            print(f" Không tìm thấy sinh viên với từ khóa '{keyword}'")
            return

        print(f"\n{'='*80}")
        print(f" KẾT QUẢ TÌM KIẾM: '{keyword}'")
        print(f"{'='*80}")
        
        for student in results:
            print(f"\n Mã: {student['id']}")
            print(f"   Tên: {student['name']}")
            print(f"   Email: {student['email']}")
            print(f"   Điện thoại: {student['phone']}")
            print(f"   GPA: {student['gpa']}")
        
        print(f"\n{'='*80}")
        print(f" Tìm thấy: {len(results)} kết quả\n")


# ============================================================
# DEMO - Sử dụng hệ thống
# ============================================================

if __name__ == "__main__":
    # Khởi tạo hệ thống quản lý sinh viên
    system = StudentManagement()
    
    # 1. Hiển thị danh sách sinh viên (định dạng bảng)
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    system.show_students()
    
    # 2. Hiển thị danh sách chi tiết
    system.show_students_detailed()
    
    # 3. Hiển thị sinh viên theo trạng thái
    system.show_students_by_status("Đang học")
    
    # 4. Hiển thị top sinh viên có GPA cao
    system.show_top_students(3)
    
    # 5. Tìm kiếm sinh viên
    system.search_student("Nguyễn")
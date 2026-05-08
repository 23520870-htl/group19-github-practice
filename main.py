import sys
sys.stdout.reconfigure(encoding='utf-8')
from todo import TaskManager
from Utils import clear_screen, display_menu, get_valid_input

def main():
    """Chương trình chính - To-do List"""
    manager = TaskManager()
    
    while True:
        clear_screen()
        print("=" * 60)
        print("   📋 TO-DO LIST - QUẢN LÝ CÔNG VIỆC")
        print("=" * 60)
        
        # Hiển thị thống kê
        total = manager.get_total_tasks()
        completed = manager.get_completed_tasks()
        pending = total - completed
        
        if total > 0:
            print(f"\n📊 Thống kê: Tổng {total} | ✅ Hoàn thành {completed} | ⏳ Chưa làm {pending}")
        
        display_menu([
            "1. ➕ Thêm công việc mới",
            "2. 📝 Hiển thị tất cả công việc",
            "3. 🔍 Hiển thị công việc chưa hoàn thành",
            "4. 🔎 Tìm kiếm công việc",
            "5. ✅ Đánh dấu hoàn thành",
            "6. ✏️  Cập nhật công việc",
            "7. 🗑️  Xóa công việc",
            "8. 🚀 Xem ưu tiên cao",
            "9. 🚪 Thoát"
        ])
        
        choice = input("\nChọn chức năng (1-9): ").strip()
        
        if choice == "1":
            add_task(manager)
        elif choice == "2":
            display_all_tasks(manager)
        elif choice == "3":
            display_pending_tasks(manager)
        elif choice == "4":
            search_task(manager)
        elif choice == "5":
            mark_completed(manager)
        elif choice == "6":
            update_task(manager)
        elif choice == "7":
            delete_task(manager)
        elif choice == "8":
            display_high_priority(manager)
        elif choice == "9":
            print("\n👋 Cảm ơn đã sử dụng To-do List!")
            break
        else:
            print("\n❌ Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")


def add_task(manager):
    """Thêm công việc mới"""
    clear_screen()
    print("=" * 60)
    print("   ➕ THÊM CÔNG VIỆC MỚI")
    print("=" * 60)
    
    try:
        title = input("\n📌 Tiêu đề công việc: ").strip()
        if not title:
            print("❌ Tiêu đề không được để trống!")
            return
        
        description = input("📝 Mô tả (nếu có): ").strip()
        
        print("\n⚡ Mức độ ưu tiên:")
        print("  1. Thấp (Low)")
        print("  2. Trung bình (Medium)")
        print("  3. Cao (High)")
        
        priority_choice = input("Chọn (1-3, mặc định 2): ").strip()
        
        priority_map = {"1": "Low", "2": "Medium", "3": "High"}
        priority = priority_map.get(priority_choice, "Medium")
        
        category = input("🏷️  Thể loại (công việc/học tập/mua sắm, mặc định 'công việc'): ").strip()
        if not category:
            category = "công việc"
        
        if manager.add_task(title, description, priority, category):
            print(f"\n✅ Thêm công việc '{title}' thành công!")
        else:
            print("\n❌ Lỗi khi thêm công việc!")
    
    except Exception as e:
        print(f"❌ Lỗi: {e}")


def display_all_tasks(manager):
    """Hiển thị tất cả công việc"""
    clear_screen()
    print("=" * 60)
    print("   📝 DANH SÁCH TẤT CẢ CÔNG VIỆC")
    print("=" * 60)
    
    tasks = manager.get_all_tasks()
    
    if not tasks:
        print("\n📭 Không có công việc nào!")
        return
    
    print(f"\n{'ID':<4} {'Trạng thái':<5} {'⚡':<5} {'Tiêu đề':<25} {'Thể loại':<12} {'Ngày tạo':<19}")
    print("-" * 85)
    
    for task in tasks:
        status = "✅" if task['completed'] else "⏳"
        priority_symbol = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}.get(task['priority'], "⚪")
        task_id = task['id']
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']
        
        print(f"{task_id:<4} {status:<5} {priority_symbol:<5} {title:<25} {task['category']:<12} {task['created_at']:<19}")
    
    print(f"\n📊 Tổng: {len(tasks)} công việc")


def display_pending_tasks(manager):
    """Hiển thị công việc chưa hoàn thành"""
    clear_screen()
    print("=" * 60)
    print("   ⏳ CÔNG VIỆC CHƯA HOÀN THÀNH")
    print("=" * 60)
    
    tasks = manager.get_pending_tasks()
    
    if not tasks:
        print("\n🎉 Không có công việc chưa hoàn thành! Tất cả xong rồi!")
        return
    
    print(f"\n{'ID':<4} {'⚡':<5} {'Tiêu đề':<30} {'Thể loại':<12} {'Tạo':<19}")
    print("-" * 85)
    
    for task in tasks:
        priority_symbol = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}.get(task['priority'], "⚪")
        title = task['title'][:28] + ".." if len(task['title']) > 30 else task['title']
        
        print(f"{task['id']:<4} {priority_symbol:<5} {title:<30} {task['category']:<12} {task['created_at']:<19}")
    
    print(f"\n⏳ Còn {len(tasks)} công việc cần làm")


def search_task(manager):
    """Tìm kiếm công việc"""
    clear_screen()
    print("=" * 60)
    print("   🔎 TÌM KIẾM CÔNG VIỆC")
    print("=" * 60)
    
    print("\n1. Tìm theo tiêu đề")
    print("2. Tìm theo thể loại")
    print("3. Tìm theo mức độ ưu tiên")
    
    choice = input("\nChọn cách tìm kiếm (1-3): ").strip()
    
    results = []
    
    if choice == "1":
        keyword = input("Nhập từ khóa: ").strip()
        results = manager.search_by_title(keyword)
    elif choice == "2":
        category = input("Nhập thể loại: ").strip()
        results = manager.search_by_category(category)
    elif choice == "3":
        print("Chọn mức độ ưu tiên: 1=Low, 2=Medium, 3=High")
        priority_choice = input("Chọn (1-3): ").strip()
        priority_map = {"1": "Low", "2": "Medium", "3": "High"}
        priority = priority_map.get(priority_choice)
        if priority:
            results = manager.search_by_priority(priority)
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    
    if not results:
        print("\n📭 Không tìm thấy công việc!")
        return
    
    print(f"\n✅ Tìm thấy {len(results)} công việc:\n")
    print(f"{'ID':<4} {'Status':<7} {'⚡':<5} {'Tiêu đề':<30} {'Thể loại':<12}")
    print("-" * 80)
    
    for task in results:
        status = "✅" if task['completed'] else "⏳"
        priority_symbol = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}.get(task['priority'], "⚪")
        title = task['title'][:28] + ".." if len(task['title']) > 30 else task['title']
        print(f"{task['id']:<4} {status:<7} {priority_symbol:<5} {title:<30} {task['category']:<12}")


def mark_completed(manager):
    """Đánh dấu công việc hoàn thành"""
    clear_screen()
    print("=" * 60)
    print("   ✅ ĐÁNH DẤU HOÀN THÀNH")
    print("=" * 60)
    
    task_id = input("\nNhập ID công việc: ").strip()
    
    if manager.mark_completed(task_id):
        print("✅ Đánh dấu hoàn thành thành công!")
    else:
        print("❌ Không tìm thấy công việc!")


def update_task(manager):
    """Cập nhật công việc"""
    clear_screen()
    print("=" * 60)
    print("   ✏️  CẬP NHẬT CÔNG VIỆC")
    print("=" * 60)
    
    task_id = input("\nNhập ID công việc: ").strip()
    task = manager.get_task_by_id(task_id)
    
    if not task:
        print("❌ Không tìm thấy công việc!")
        return
    
    print(f"\n📌 Công việc hiện tại: {task['title']}")
    print(f"Mô tả: {task['description']}")
    print(f"Ưu tiên: {task['priority']}")
    
    print("\n1. Cập nhật tiêu đề")
    print("2. Cập nhật mô tả")
    print("3. Cập nhật mức độ ưu tiên")
    print("4. Cập nhật thể loại")
    
    choice = input("\nChọn (1-4): ").strip()
    
    try:
        if choice == "1":
            new_title = input("Tiêu đề mới: ").strip()
            if manager.update_task(task_id, title=new_title):
                print("✅ Cập nhật thành công!")
        elif choice == "2":
            new_desc = input("Mô tả mới: ").strip()
            if manager.update_task(task_id, description=new_desc):
                print("✅ Cập nhật thành công!")
        elif choice == "3":
            print("Chọn: 1=Low, 2=Medium, 3=High")
            priority_choice = input("Chọn (1-3): ").strip()
            priority_map = {"1": "Low", "2": "Medium", "3": "High"}
            priority = priority_map.get(priority_choice)
            if priority and manager.update_task(task_id, priority=priority):
                print("✅ Cập nhật thành công!")
        elif choice == "4":
            new_category = input("Thể loại mới: ").strip()
            if manager.update_task(task_id, category=new_category):
                print("✅ Cập nhật thành công!")
        else:
            print("❌ Lựa chọn không hợp lệ!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")


def delete_task(manager):
    """Xóa công việc"""
    clear_screen()
    print("=" * 60)
    print("   🗑️  XÓA CÔNG VIỆC")
    print("=" * 60)
    
    task_id = input("\nNhập ID công việc: ").strip()
    task = manager.get_task_by_id(task_id)
    
    if not task:
        print("❌ Không tìm thấy công việc!")
        return
    
    print(f"\n❓ Bạn chắc chắn muốn xóa: '{task['title']}'?")
    confirm = input("Xác nhận (y/n): ").strip().lower()
    
    if confirm == 'y':
        if manager.delete_task(task_id):
            print("✅ Xóa thành công!")
        else:
            print("❌ Lỗi khi xóa!")
    else:
        print("⚠️  Đã hủy xóa!")


def display_high_priority(manager):
    """Hiển thị công việc ưu tiên cao"""
    clear_screen()
    print("=" * 60)
    print("   🚀 CÔNG VIỆC ƯU TIÊN CAO")
    print("=" * 60)
    
    tasks = manager.search_by_priority("High")
    
    if not tasks:
        print("\n✅ Không có công việc ưu tiên cao!")
        return
    
    pending_tasks = [t for t in tasks if not t['completed']]
    
    if not pending_tasks:
        print("\n✅ Tất cả công việc ưu tiên cao đã hoàn thành!")
        return
    
    print(f"\n{'ID':<4} {'Status':<7} {'Tiêu đề':<35} {'Thể loại':<12} {'Tạo':<19}")
    print("-" * 85)
    
    for task in pending_tasks:
        status = "✅" if task['completed'] else "🔴 URGENT"
        title = task['title'][:33] + ".." if len(task['title']) > 35 else task['title']
        print(f"{task['id']:<4} {status:<7} {title:<35} {task['category']:<12} {task['created_at']:<19}")
    
    print(f"\n🚨 {len(pending_tasks)} công việc cần ưu tiên!")


if __name__ == "__main__":
    main()
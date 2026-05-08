import os
import sys


def clear_screen():
    """Xóa màn hình console"""
    os.system('clear' if os.name == 'posix' else 'cls')


def display_menu(options):
    """Hiển thị menu với các tùy chọn"""
    for option in options:
        print(f"  {option}")


def get_valid_input(prompt, data_type=str, min_val=None, max_val=None):
    """
    Lấy input hợp lệ từ người dùng
    
    Args:
        prompt: Thông báo nhập
        data_type: Kiểu dữ liệu (str, int, float)
        min_val: Giá trị tối thiểu (cho int/float)
        max_val: Giá trị tối đa (cho int/float)
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input:
                print("❌ Vui lòng nhập giá trị!")
                continue
            
            if data_type == int:
                value = int(user_input)
                if min_val is not None and value < min_val:
                    print(f"❌ Giá trị phải >= {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"❌ Giá trị phải <= {max_val}")
                    continue
                return value
            
            elif data_type == float:
                value = float(user_input)
                if min_val is not None and value < min_val:
                    print(f"❌ Giá trị phải >= {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"❌ Giá trị phải <= {max_val}")
                    continue
                return value
            
            else:
                return user_input
        
        except ValueError:
            print(f"❌ Nhập không hợp lệ! Vui lòng nhập {data_type.__name__}")


def print_header(title, width=50):
    """In tiêu đề với khung"""
    print("\n" + "=" * width)
    print(f"  {title}".center(width))
    print("=" * width)


def print_success(message):
    """In thông báo thành công"""
    print(f"\n✅ {message}")


def print_error(message):
    """In thông báo lỗi"""
    print(f"\n❌ {message}")


def print_warning(message):
    """In cảnh báo"""
    print(f"\n⚠️  {message}")


def print_info(message):
    """In thông tin"""
    print(f"\nℹ️  {message}")


def format_table(headers, rows):
    """
    Định dạng và in bảng
    
    Args:
        headers: Danh sách header
        rows: Danh sách các hàng dữ liệu
    """
    # Tính độ rộng cột
    col_widths = [len(str(h)) for h in headers]
    
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # In header
    header_row = " | ".join(
        str(h).ljust(col_widths[i]) for i, h in enumerate(headers)
    )
    print(header_row)
    print("-" * len(header_row))
    
    # In rows
    for row in rows:
        print(" | ".join(
            str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)
        ))


def format_percentage(value, max_value):
    """Định dạng phần trăm"""
    if max_value == 0:
        return "0%"
    percentage = (value / max_value) * 100
    return f"{percentage:.1f}%"


def separator(char="-", length=60):
    """In đường phân cách"""
    print(char * length)


def input_yes_no(prompt="Xác nhận (y/n): "):
    """Yêu cầu xác nhận có/không"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes', 'có', 'co']:
            return True
        elif answer in ['n', 'no', 'không', 'khong']:
            return False
        else:
            print("Vui lòng nhập 'y' hoặc 'n'")


def pause(message="Nhấn Enter để tiếp tục..."):
    """Tạm dừng và chờ nhập Enter"""
    input(f"\n{message}")


def print_with_delay(message, delay=0.05):
    """In từng ký tự với độ trễ (hiệu ứng gõ)"""
    import time
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


class Colors:
    """Màu sắc cho terminal (ANSI codes)"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colored_text(text, color):
    """In text có màu"""
    return f"{color}{text}{Colors.ENDC}"


def print_progress_bar(iteration, total, prefix='', suffix='', length=30):
    """In thanh tiến trình"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = '█' * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='')
    if iteration == total:
        print()
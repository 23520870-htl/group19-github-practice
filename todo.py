import json
import os
from datetime import datetime


class Task:
    """Lớp đại diện cho một công việc"""
    
    _counter = 1000  # ID tự tăng
    
    def __init__(self, title, description="", priority="Medium", category="công việc"):
        Task._counter += 1
        self.id = str(Task._counter)
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None
    
    def mark_completed(self):
        """Đánh dấu công việc hoàn thành"""
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_incomplete(self):
        """Đánh dấu công việc chưa hoàn thành"""
        self.completed = False
        self.completed_at = None
    
    def to_dict(self):
        """Chuyển đối tượng Task thành dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'category': self.category,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    def __str__(self):
        status = "✅" if self.completed else "⏳"
        return f"{status} [{self.id}] {self.title} ({self.priority})"


class TaskManager:
    """Lớp quản lý danh sách công việc"""
    
    def __init__(self, filename='tasks_data.json'):
        self.filename = filename
        self.tasks = self.load_data()
        # Cập nhật counter nếu có dữ liệu cũ
        if self.tasks:
            max_id = max(int(task_id) for task_id in self.tasks.keys())
            Task._counter = max_id
    
    def load_data(self):
        """Tải dữ liệu từ file JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_data(self):
        """Lưu dữ liệu vào file JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"❌ Lỗi khi lưu dữ liệu: {e}")
            return False
    
    def add_task(self, title, description="", priority="Medium", category="công việc"):
        """Thêm công việc mới"""
        try:
            task = Task(title, description, priority, category)
            self.tasks[task.id] = task.to_dict()
            self.save_data()
            return True
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            return False
    
    def get_all_tasks(self):
        """Lấy tất cả công việc"""
        return list(self.tasks.values())
    
    def get_task_by_id(self, task_id):
        """Lấy công việc theo ID"""
        return self.tasks.get(task_id)
    
    def get_pending_tasks(self):
        """Lấy danh sách công việc chưa hoàn thành"""
        return [task for task in self.tasks.values() if not task['completed']]
    
    def get_completed_tasks_list(self):
        """Lấy danh sách công việc đã hoàn thành"""
        return [task for task in self.tasks.values() if task['completed']]
    
    def search_by_title(self, keyword):
        """Tìm công việc theo tiêu đề"""
        results = []
        keyword_lower = keyword.lower()
        
        for task in self.tasks.values():
            if keyword_lower in task['title'].lower():
                results.append(task)
        
        return results
    
    def search_by_category(self, category):
        """Tìm công việc theo thể loại"""
        results = []
        category_lower = category.lower()
        
        for task in self.tasks.values():
            if category_lower in task['category'].lower():
                results.append(task)
        
        return results
    
    def search_by_priority(self, priority):
        """Tìm công việc theo mức độ ưu tiên"""
        return [task for task in self.tasks.values() if task['priority'] == priority]
    
    def mark_completed(self, task_id):
        """Đánh dấu công việc hoàn thành"""
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            self.tasks[task_id]['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_data()
            return True
        return False
    
    def mark_incomplete(self, task_id):
        """Đánh dấu công việc chưa hoàn thành"""
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = False
            self.tasks[task_id]['completed_at'] = None
            self.save_data()
            return True
        return False
    
    def update_task(self, task_id, title=None, description=None, priority=None, category=None):
        """Cập nhật thông tin công việc"""
        if task_id not in self.tasks:
            return False
        
        if title is not None:
            self.tasks[task_id]['title'] = title
        if description is not None:
            self.tasks[task_id]['description'] = description
        if priority is not None:
            self.tasks[task_id]['priority'] = priority
        if category is not None:
            self.tasks[task_id]['category'] = category
        
        self.save_data()
        return True
    
    def delete_task(self, task_id):
        """Xóa công việc"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_data()
            return True
        return False
    
    def get_total_tasks(self):
        """Lấy tổng số công việc"""
        return len(self.tasks)
    
    def get_completed_tasks(self):
        """Lấy số công việc đã hoàn thành"""
        return sum(1 for task in self.tasks.values() if task['completed'])
    
    def get_pending_count(self):
        """Lấy số công việc chưa hoàn thành"""
        return self.get_total_tasks() - self.get_completed_tasks()
    
    def get_tasks_by_priority(self):
        """Lấy thống kê công việc theo mức độ ưu tiên"""
        stats = {"Low": 0, "Medium": 0, "High": 0}
        
        for task in self.tasks.values():
            if task['priority'] in stats:
                stats[task['priority']] += 1
        
        return stats
    
    def get_completion_rate(self):
        """Lấy tỷ lệ hoàn thành"""
        if self.get_total_tasks() == 0:
            return 0
        
        completed = self.get_completed_tasks()
        total = self.get_total_tasks()
        
        return round((completed / total) * 100, 2)
    
    def clear_all(self):
        """Xóa tất cả công việc (cẩn thận!)"""
        self.tasks = {}
        self.save_data()
        return True
    
    def clear_completed(self):
        """Xóa tất cả công việc đã hoàn thành"""
        completed_ids = [task_id for task_id, task in self.tasks.items() if task['completed']]
        
        for task_id in completed_ids:
            del self.tasks[task_id]
        
        self.save_data()
        return len(completed_ids)
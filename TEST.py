# todo_manager.py
"""
Simple To-Do List Manager
A test project for GitHub
"""

import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)
    
    def add_task(self, title, description=""):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: {title}")
    
    def list_tasks(self, show_completed=True):
        """Display all tasks"""
        if not self.tasks:
            print("\n📭 No tasks found!")
            return
        
        print("\n" + "="*50)
        print("📋 YOUR TASKS")
        print("="*50)
        
        for task in self.tasks:
            if not show_completed and task['completed']:
                continue
            
            status = "✓" if task['completed'] else "◻"
            print(f"\n[{status}] {task['id']}. {task['title']}")
            if task['description']:
                print(f"    📝 {task['description']}")
            print(f"    🕐 Created: {task['created_at']}")
        
        print("\n" + "="*50)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"⚠ Task already completed!")
                else:
                    task['completed'] = True
                    self.save_tasks()
                    print(f"🎉 Task completed: {task['title']}")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                # Reorder IDs
                for idx, t in enumerate(self.tasks):
                    t['id'] = idx + 1
                self.save_tasks()
                print(f"🗑 Deleted task: {deleted['title']}")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def clear_all(self):
        """Delete all tasks"""
        confirm = input("⚠ Delete ALL tasks? (yes/no): ")
        if confirm.lower() == 'yes':
            self.tasks = []
            self.save_tasks()
            print("✅ All tasks cleared!")
        else:
            print("❌ Operation cancelled")


def main():
    manager = TodoManager()
    
    while True:
        print("\n" + "🔧 TO-DO LIST MANAGER".center(50))
        print("1. 📝 Add task")
        print("2. 📋 List all tasks")
        print("3. ✅ Complete task")
        print("4. 🗑 Delete task")
        print("5. 🧹 Clear all tasks")
        print("6. 🚪 Exit")
        
        choice = input("\nChoose option (1-6): ").strip()
        
        if choice == '1':
            title = input("Task title: ").strip()
            if title:
                desc = input("Description (optional): ").strip()
                manager.add_task(title, desc)
            else:
                print("❌ Title cannot be empty!")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            manager.list_tasks()
            try:
                task_id = int(input("\nEnter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '4':
            manager.list_tasks()
            try:
                task_id = int(input("\nEnter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '5':
            manager.clear_all()
        
        elif choice == '6':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid option! Please choose 1-6")


if __name__ == "__main__":
    main()

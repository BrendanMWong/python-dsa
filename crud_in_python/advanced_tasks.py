import time
import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create(self, description):
        self.tasks[self.next_id] = \
        {"description": description, 
         "timestamp": time.time(),
         "status": "pending"}
        temp = self.next_id
        self.next_id += 1
        return temp

    def read(self, task_id):
        return self.tasks.get(task_id)

    def update(self, task_id, description=None):
        if task_id not in self.tasks:
            return None
        if description is not None:
            self.tasks[task_id]["description"] = description
        return self.tasks[task_id]

    def delete(self, task_id):
        return self.tasks.pop(task_id, None)
    
    def update_status(self, task_id, status):
        task = self.tasks.get(task_id, None)
        if task is None:
            return None
        if status in ["pending", "in_progress", "completed"]:
            task["status"] = status
            return task
        else:
            return False
    
    def get_tasks_by_status(self, status):
        if status not in ["pending", "in_progress", "completed"]:
            return []
        return [task for task in self.tasks.values() if task["status"] == status]
    
    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                json_string = json.dumps(self.tasks)
                file.write(json_string)
            return True
        except:
            return False

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                python_string = json.loads(file)
                self.tasks = python_string
            return True
        except:
            return False
        
if __name__ == "__main__":
    manager = TaskManager()

    print("=== PART 1: CRUD ===")
    id1 = manager.create("Task A")
    id2 = manager.create("Task B")

    print("All tasks after creation:")
    print(manager.tasks)

    print("\nRead task 1:")
    print(manager.read(id1))

    manager.update(id1, "Task A Updated")
    print("\nAfter update:")
    print(manager.read(id1))

    manager.delete(id2)
    print("\nAfter delete:")
    print(manager.tasks)

    print("\n=== PART 2: STATUS UPDATE ===")
    result = manager.update_status(id1, "completed")
    print("Update status result:")
    print(result)

    print("Invalid status test:")
    print(manager.update_status(id1, "invalid_status"))

    print("\nTask after status update:")
    print(manager.read(id1))

    print("\n=== PART 3: FILTERING ===")
    id3 = manager.create("Task C")
    manager.update_status(id3, "pending")

    print("Tasks with status 'pending':")
    print(manager.get_tasks_by_status("pending"))

    print("Tasks with status 'completed':")
    print(manager.get_tasks_by_status("completed"))

    print("Invalid filter test:")
    print(manager.get_tasks_by_status("not_a_status"))
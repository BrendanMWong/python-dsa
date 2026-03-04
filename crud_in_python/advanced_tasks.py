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
                data = json.load(file)
            # normalize keys to int
            self.tasks = {int(key): value for key, value in data.items()}
            # reset next_id
            if self.tasks:
                self.next_id = max(self.tasks.keys()) + 1
            else:
                self.next_id = 1
            return True
        except:
            return False
        
    def search_by_description(self, keyword: str) -> list[dict]: 
        output = []
        if not keyword:
            return output
        keyword = keyword.lower()
        for task in self.tasks.values():
            task_description = task["description"].lower()
            if keyword in task_description:
                output.append(task)
        return output
    
    def sort_by_timestamp(self) -> list[dict]:
        # syntax: sorted(iterable, optional key = call by this function, optional reverse = bool)
        # self.tasks.values() are all the tasks
        return sorted(self.tasks.values(), key = self._get_timestamp)
    
    # _function: for internal use only
    def _get_timestamp(self, task: dict) -> float:
        return task["timestamp"]
        
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "tasks.json")

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

    print("\n=== PART 4: PERSISTENCE ===")

    print("Saving to file...")
    print(manager.save_to_file(file_path))

    # Create new manager to simulate restart
    new_manager = TaskManager()

    print("Loading from file...")
    print(new_manager.load_from_file(file_path))

    print("Loaded tasks:")
    print(new_manager.tasks)

    print("Next ID after loading:")
    print(new_manager.next_id)

    print("\n=== PART 5: SEARCH ===")

    # Create tasks with distinct text
    manager.create("Write quarterly report")
    manager.create("Email project update")
    manager.create("Write unit tests")

    print("Search for 'write':")
    print(manager.search_by_description("write"))

    print("Search for 'EMAIL': (case-insensitive test)")
    print(manager.search_by_description("EMAIL"))

    print("Search with empty string:")
    print(manager.search_by_description(""))

    print("\n=== PART 6: SORTING ===")

    # Clear and rebuild for clean timestamp order test
    manager = TaskManager()

    manager.create("First task")
    time.sleep(1)
    manager.create("Second task")
    time.sleep(1)
    manager.create("Third task")

    print("Tasks sorted by timestamp (oldest first):")
    sorted_tasks = manager.sort_by_timestamp()
    for task in sorted_tasks:
        print(task)
    

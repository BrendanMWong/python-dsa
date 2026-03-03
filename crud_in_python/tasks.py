import time

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create(self, description):
        self.tasks[self.next_id] = {"description": description, "timestamp": time.time()}
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

if __name__ == "__main__":
    manager = TaskManager()

    # Create tasks
    id1 = manager.create("Finish CodeSignal practice")
    id2 = manager.create("Apply to internships")

    print("After creation:")
    print(manager.tasks)

    # Read
    print("\nRead task:", manager.read(id1))

    # Update
    manager.update(id1, "Finish CodeSignal practice (seriously)")
    print("\nAfter update:")
    print(manager.read(id1))

    # Delete
    manager.delete(id2)
    print("\nAfter delete:")
    print(manager.tasks)

    # Attempt to read deleted task
    print("\nRead deleted task:", manager.read(id2))
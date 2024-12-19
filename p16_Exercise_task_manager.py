class Task:
    _description = ""
    _completed = False

    def __init__(self, description_, completed_=False):
        self.description = description_
        self.completed = completed_

    def __repr__(self):
        return f"Task(description={self.description}, completed={self.completed})"

    def __str__(self):
        return f"Task: {self.description}, completed={self.completed}"

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description_):
        self._description = description_

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed_):
        if not isinstance(completed_, bool):
            raise TypeError
        self._completed = completed_

    def mark_completed(self):
        self.completed = True


class TaskManager:
    _tasks = []

    def __init__(self):
        self._tasks = []

    def __repr__(self):
        return f"TaskManager({self.tasks})"

    def __str__(self):
        return f"TaskManager with {len(self.tasks)} tasks."

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks_):
        self._tasks = tasks_

    def add_task(self, task_):
        self.tasks.append(task_)

    def mark_completed(self, i):
        self.tasks[i].mark_completed()

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]


if __name__ == "__main__":
    manager = TaskManager()
    task1 = Task("Complete assignment")
    print(task1)
    task2 = Task("Read book")
    print(task2)
    manager.add_task(task1)
    print(manager)
    manager.add_task(task2)
    print(manager)
    print(f"Completed tasks: {manager.get_completed_tasks()}")
    print(f"Incomplete tasks: {manager.get_incomplete_tasks()}")
    task1.mark_completed()
    print('-'*80)
    print(f"Completed tasks: {manager.get_completed_tasks()}")
    print(f"Incomplete tasks: {manager.get_incomplete_tasks()}")
    manager.mark_completed(1)
    print('-'*80)
    print(f"Completed tasks: {manager.get_completed_tasks()}")
    print(f"Incomplete tasks: {manager.get_incomplete_tasks()}")

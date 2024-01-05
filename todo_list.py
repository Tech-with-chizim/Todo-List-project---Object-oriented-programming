class Task:
    def __init__(self, title, description, completed=False):
        # Initialize Task object with title, description, and completion status (default is False)
        self.title = title
        self.description =  description
        self.completed  = completed
    
    def __str__(self):
        # Provide a string representation of the Task object, including completion status
        status  =  "completed" if self.completed else "Not completed"
        return f'{self.title} - { self.description} ({status})'

class Todo_list:
    def __init__(self):
        # Initialize Todo_list object with an empty list of tasks
        self.tasks = []

    def add_task(self, title, description):
        # Create a Task object and add it to the list of tasks
        task = Task(title, description)
        self.tasks.append(task)
    
    def remove_task(self, title):
        # Remove tasks with the specified title from the list
        self.tasks = [task for task in self.tasks if task.title != title]
    
    def mark_complete(self, title):
        # Mark a task with the specified title as completed
        for task in self.tasks:
            if task.title == title:
                task.completed = True
    
    def display_todo(self):
        # Display all tasks in the Todo_list
        for task in self.tasks:
            print(task)

if __name__ == "__main__":
    # Create an instance of Todo_list
    todo_list = Todo_list()

# Adding tasks to the Todo_list
todo_list.add_task('gaming', 'duration 1hr 4pm - 5pm')    
todo_list.add_task('general studies', "duration = 2hrs")
todo_list.add_task('coding', '2hrs of scripting and automation')
todo_list.add_task('music', 'practice with the Grand piano')

print('Initial tasks:')
todo_list.display_todo()

# Marking a task as completed and removing a task
todo_list.mark_complete('gaming')
todo_list.remove_task('music')

print('\nAfter manipulation:')
todo_list.display_todo()


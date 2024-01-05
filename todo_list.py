class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description =  description
        self.completed  = completed
    
    def __str__(self):
        status  =  "completed" if self.completed else "Not completed"
        return f'{self.title} - { self.description} ({status})'

class Todo_list:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
    
    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
    
    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
    
    def display_todo(self):
        for task in self.tasks:
            print (task)

if __name__ == "__main__":
    Todo_list = Todo_list()

Todo_list.add_task('gaming', 'duration 1hr  4pm -5pm')    
Todo_list.add_task('general studies', "duration =  2hrs")
Todo_list.add_task('coding', '2hrs of scripting and automation')
Todo_list.add_task('music', 'practice with the Grand piano')
print('initial tasks')
Todo_list.display_todo()
print()
Todo_list.mark_complete('gaming')
Todo_list.remove_task('music')
print()
print('after manupilaton')
Todo_list.display_todo()

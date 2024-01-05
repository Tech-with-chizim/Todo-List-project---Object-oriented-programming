# Todo List Script in Python

This Python script implements a basic Todo list using Object-Oriented Programming (OOP) principles. It consists of two classes: `Task` and `Todo_list`.

## Task Class

- Represents an individual task with attributes like title, description, and completion status.
- The `__str__` method provides a clear string representation of the task, including its completion status.

## Todo_list Class

- Manages a list of tasks and provides methods for adding tasks, removing tasks, marking tasks as complete, and displaying the current tasks.

## Example Usage

```python
from todo_script import Todo_list

todo_list = Todo_list()

todo_list.add_task('gaming', 'duration 1hr 4pm - 5pm')    
todo_list.add_task('general studies', 'duration = 2hrs')
todo_list.add_task('coding', '2hrs of scripting and automation')
todo_list.add_task('music', 'practice with the Grand piano')

print('Initial tasks:')
todo_list.display_todo()

todo_list.mark_complete('gaming')
todo_list.remove_task('music')

print('\nAfter manipulation:')
todo_list.display_todo()

# the msg variable for user to enter the to do
prompt = "Enter to do:"

# define an empty list outside the while loop
todos = []

# while True ask user to enter the to do.
# use title method to format each to do
# append each to do to empty list
# print a list of all the todos
while True:
    todo = input(prompt)
    todo = todo.title()
    todos.append(todo)
    print(todos)

# user input
# Task1 = input(prompt)
# Task2 = input(prompt)
# Task3 = input(prompt)
#
# Todolist = [Task1, Task2, Task3]
# print(Todolist)
#
# print(type(Todolist))
#
# print("Length of the task1:", len(Task1))
# print("Length of the task2:", len(Task2))
# print("Length of the task3:", len(Task3))
#

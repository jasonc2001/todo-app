def write_todos(todos_arg=None, filepath="files/todos.txt"):
    """ Write todos_arg item list into the text file"""
    with open(filepath, 'w') as file_name:
        file_name.writelines(todos_arg)


def read_todos(filepath="files/todos.txt"):
    with open("files/todos.txt", 'r') as file:
        todos = file.readlines()
    return todos

from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space characters from it
    usr_action = input("Type add, show, edit, complete, delete or exit: ")
    usr_action = usr_action.strip()
    # Open/Create the file then read it

    todos = functions.read_todos()

    # check if user action is "add"
    if usr_action.startswith("add"):
        todo = usr_action[4:] + '\n'
        todos.append(todo.title())

        functions.write_todos(todos)

    elif usr_action.startswith("show"):
        for i, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            out = f"{i + 1}. {item}"
            print(out)

    elif usr_action.startswith("edit"):
        try:
            number = int(usr_action[5:])
            number -= 1
            new_todo = input("Enter your change: ") + '\n'
            todos[number] = new_todo.title()
            functions.write_todos(todos)
            print("After changing: ", todos)
        except ValueError:
            print("Your input is invalid.")
            continue

    elif usr_action.startswith("complete"):
        try:
            number = int(usr_action[9:])
            todo_removed = todos.pop(number - 1)

            functions.write_todos(todos)

            print(f'"{todo_removed.title().strip()}" was removed from the list')
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("ValueError")

    elif 'exit' == usr_action:
        break

    else:
        print("Please enter a known command")

print("Bye!")

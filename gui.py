from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My To-do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button]
                           [exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.read_todos()
            todo = values["todo"].title() + '\n'
            todos.append(todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo = values['todos'][0]
            new_todo = values['todo'].title() + '\n'

            todos = functions.read_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.read_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()

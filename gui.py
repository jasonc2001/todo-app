from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo")
add_botton = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_botton]])
window.read()
window.close()

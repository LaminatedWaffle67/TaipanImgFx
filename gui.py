import tkinter as tk
import config, threading, queue, inspect, ast, sys
from TaipanCode.AllEffects import edit, color, spatial

ignore_functions = ['color.print()'] # functions I do not need in the function list
total_function_list = []
for name, function in inspect.getmembers(edit, inspect.isfunction):
    total_function_list.append("edit." + str(name) + "()")

for name, function in inspect.getmembers(color, inspect.isfunction):
    total_function_list.append("color." + str(name) + "()")

for name, function in inspect.getmembers(spatial, inspect.isfunction):
    total_function_list.append("spatial." + str(name) + "()")

copy_list = [] # makes a temporary empty list 

for name in total_function_list:
    if name not in ignore_functions:
        copy_list.append((name))

total_function_list = copy_list


def parameter_button(parent_effect, parameter_index):
    signature = inspect.signature(parent_effect)
    sig_parameters = signature.parameters
    sig_parameters_name_list = list(sig_parameters)
    sig_parameters_list = list(sig_parameters.values())
    sig_parameters_tuple = ()

    for current_param in sig_parameters_list:
        annotated = current_param.annotation
        current_input = input(f"{current_param}\n>")
        try:

            if annotated != inspect._empty:
                current_input = annotated(current_input)
            else:
                raise RuntimeError(f"{current_param}: {current_input} could not be resolved as the annotation is {annotated}.")

            
        except Exception as e:
            print (f"Error: Could not convert {current_input} to {annotated}\nError Msg -> {e}")
            sys.exit()

        sig_parameters_tuple += (current_input, )

    func_parameter_list[parameter_index] = sig_parameters_tuple



def enqueue(lambda_func): 
    config.effect_queue.put(lambda_func)

copy_list = []
for i in range(len(total_function_list)):
    iter_str = ""
    for char in total_function_list[i]:
        if char != '(' and char != ')':
            iter_str += char

    copy_list.append(iter_str)

total_function_list = copy_list

copy_list = []
for name in total_function_list:
    parent_module, child_func = name.split('.', 1)
    copy_list.append((name, parent_module, child_func))

total_function_list = copy_list

function_names = [(name, getattr(globals()[p_mod], c_func)) for name, p_mod, c_func in total_function_list]
func_parameter_list = [None for i in range(len(function_names))]

# --Page button management functions--
def show_page(old_page_index, page_index, button_list, effect_window):
    if old_page_index is not None:
        for current_button in button_list[old_page_index]:
            current_button.grid_remove()

    for i, current_button in enumerate(button_list[page_index]):
        current_button.grid(row=i, column=1, padx=5, pady=5)

        func_ref = function_names[i][1]
        current_param_button = tk.Button(effect_window, text="<", command=lambda f=func_ref, j=i: parameter_button(f, j))
        current_param_button.grid(row=i, column=0, padx=5, pady=5)
        
# --Page button management functions--

# --Page management functions--
def toggle_buttons(direction_index, button_list, text_label, effect_window):
    global page_number

    if direction_index == 1:
        if (page_number + 1) < len(button_list):
            show_page(page_number, page_number + 1, button_list, effect_window)
            page_number += 1

    elif direction_index == 0:
        if (page_number - 1) >= 0:
            show_page(page_number, page_number - 1, button_list, effect_window)
            page_number -= 1

    text_label.config(text=f"{page_number + 1}/{len(button_list)}")
    

# --Page management functions--

# --Page settings variables--
page_number = 0
page_size = 6 - 1
# --Page settings variables--


def start_gui():
    root = tk.Tk()

    effect_window = tk.Frame(root)
    effect_window.grid(column=0, row=0)
    button_list = [[]]

    count = -1
    for i, (call, func_ref) in enumerate(function_names):
        current_button = tk.Button(effect_window, text=call, command=lambda f=func_ref, j=i: enqueue(lambda: f() if func_parameter_list[j] == None else print(func_parameter_list[j])))
        

        count += 1
        if count <= page_size:
            button_list[-1].append(current_button)

        else:
            count = 0
            button_list.append([])
            button_list[-1].append(current_button)

    
    # --Sets up the page change buttons and page count--
    toggle_frame = tk.Frame(root)
    toggle_frame.grid(column=0, row=1, pady=5)

    text_label1 = tk.Label(toggle_frame, text=f"{page_number + 1}/{len(button_list)}")
    text_label1.grid(column=1, row=0)

    def a_dispatcher():
        toggle_buttons(1, button_list, text_label1, effect_window)

    def b_dispatcher():
        toggle_buttons(0, button_list, text_label1, effect_window)

    toggle_btn1 = tk.Button(toggle_frame, text="<", command=b_dispatcher)
    toggle_btn1.grid(column=0, row=0)

    toggle_btn2 = tk.Button(toggle_frame, text=">", command=a_dispatcher)
    toggle_btn2.grid(column=2, row=0)
    # --Sets up the page change buttons and pgae count--

    # --Starts the main loop for root which is the main window--
    show_page(None, page_number, button_list, effect_window)
    root.mainloop()
    # --Starts the main loop for root which is the main window--

if __name__ == "__main__":
    start_gui()
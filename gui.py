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



def start_gui():
    root = tk.Tk()
    root.withdraw()

    effect_window = tk.Toplevel(root)

    for i, (call, func_ref) in enumerate(function_names):
        current_button = tk.Button(effect_window, text=call, command=lambda f=func_ref, j=i: enqueue(lambda: f() if func_parameter_list[j] == () else f(func_parameter_list[j])))
        current_param_button = tk.Button(effect_window, text="<", command=lambda f=func_ref, j=i: parameter_button(f, j))

        current_button.grid(row=i, column=1, padx=5, pady=5)
        current_param_button.grid(row=i, column=0, padx=5, pady=5)


    root.mainloop()

if __name__ == "__main__":
    start_gui()
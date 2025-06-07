import tkinter as tk
import config, threading, queue, inspect
from TaipanCode.AllEffects import edit, color, spatial

def parameter_button(parent_effect):
    signature = inspect.signature(parent_effect)
    parameters = signature.parameters
    parameters_list = list(parameters)

    for i in range(len(parameters)):
        current_input = input(f"{parameters_list[i]}\n>")


def enqueue(lambda_func): 
    config.effect_queue.put(lambda_func)

function_names = [("edit.clear()", edit.clear), ("color.np_invert()", color.np_invert), ("color.np_black_and_white()", color.np_black_and_white)]

def start_gui():
    root = tk.Tk()
    root.withdraw()

    effect_window = tk.Toplevel(root)

    for name, func_ref in function_names:
        current_button = tk.Button(effect_window, text=name, command=lambda f=func_ref: enqueue(lambda: f)).pack()
        current_param_button = tk.Button(effect_window, text="< " + str(name), command=lambda f=func_ref: parameter_button(f)).pack()


    root.mainloop()

if __name__ == "__main__":
    start_gui()
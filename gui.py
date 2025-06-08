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

    for i, (name, func_ref) in enumerate(function_names):
        current_button = tk.Button(effect_window, text=name, command=lambda f=func_ref: enqueue(lambda: f))
        current_param_button = tk.Button(effect_window, text="<", command=lambda f=func_ref: parameter_button(f))

        current_button.grid(row=i, column=1, padx=5, pady=5)
        current_param_button.grid(row=i, column=0, padx=5, pady=5)


    root.mainloop()

if __name__ == "__main__":
    start_gui()
import tkinter as tk
import config, threading, queue, inspect, ast, sys
from TaipanCode.AllEffects import edit, color, spatial

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

function_names = [("edit.clear()", edit.clear), ("color.np_invert()", color.np_invert), ("color.np_black_and_white()", color.np_black_and_white)]
func_parameter_list = [(), (), ()]

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
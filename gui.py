import tkinter as tk
import config, threading, queue
from TaipanCode.AllEffects import edit, color, spatial


def enqueue(lambda_func): 
    config.effect_queue.put(lambda_func)

def start_gui():
    # make root window
    root = tk.Tk()
    # make effect window
    effect_window = tk.Toplevel(root)
    # make button that runs enqueu with lambda for effetc func
    tk.Button(effect_window, text="edit.clear()", command=lambda: enqueue(lambda: edit.clear(255))).pack()
    # run mainloop
    root.mainloop()

if __name__ == "__main__":
    start_gui()
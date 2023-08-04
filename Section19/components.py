import tkinter as tk


root = tk.Tk()


tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="x") 
tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="y")


root.mainloop()

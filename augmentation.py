import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()
style.configure('TButton', borderwidth=2, relief="raised", bordercolor="white", foreground="black", background="white", focuscolor="white", focusthickness=1, highlightthickness=0, lightcolor="white", padding=6, font=('Helvetica', 12), relief="flat", anchor="center")

style.map('TButton', foreground=[('active', 'black')], background=[('active', 'white')])

button = ttk.Button(root, text="Click Me")
button.pack(pady=20, padx=50)

style.configure('TButton', borderwidth=2, relief="raised", bordercolor="white", foreground="black", background="white", focuscolor="white", focusthickness=1, highlightthickness=0, lightcolor="white", padding=6, font=('Helvetica', 12), relief="flat", anchor="center", **{'border-radius': '20px'})

root.mainloop()

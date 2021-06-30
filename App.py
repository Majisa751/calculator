import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('firstpython')
window.minsize(width=400, height=450)

title_label = tk.Label(master=window, text='เมากาว')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='kk', command=set_message)
ok_button.pack()

window.mainloop()
import tkinter as tk

def show_output():
    number = int(number_input.get())
    
    if number == 0:
         output_label.configure(text='lol')
         return 
    
    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' +str(number * i) + '\n'
        
        output_label.configure(text=output)
        
window  = tk.Tk()
window.title('Calculator')
window.minsize(width=450, height=500)


title_label = tk.Label(master=window, text='เครื่องคิดเลข')
title_label.pack(pady=20)

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(
    master=window, text='คำตอบ',
    command=show_output
    )
go_button.pack(pady=5)

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
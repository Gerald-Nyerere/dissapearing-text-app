import tkinter as tk
 
window = tk.Tk()
window.title("Disappearing Text Writing App")
window.minsize(500, 500)
counter = 0
 
def disappear_text():
    global counter
    if counter <= 10:
        alpha = 1.0 - counter * 0.1
        red = int(255 * alpha)
        color = f'#{red:02x}0000' 
        textbox.config(fg=color)
        textbox.after(200, disappear_text)
        counter += 1
    else:
        textbox.delete(1.0, tk.END)
 
def check_disappear(event=None):
    global counter, text
    if text == textbox.get(1.0, tk.END):
        if counter == 10:
            disappear_text()
            counter = -1
        window.after(1000, check_disappear)
        counter += 1
    else:
        text = textbox.get(1.0, tk.END)
        counter = 0
        window.after(1000, check_disappear)
 
def on_text_change(event):
    global counter
    counter = 0
 
title = tk.Label(window, text="Welcome to the Disappearing Text Writing App.")
title.grid(row=0, column=1)
 
text = ""
textbox = tk.Text(height=500, width=300, yscrollcommand=True)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)
 
textbox.bind("<Key>", on_text_change)  
 
window.after(1000, check_disappear)
window.mainloop()
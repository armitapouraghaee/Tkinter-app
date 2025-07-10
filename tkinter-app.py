import tkinter as tk

window = tk.Tk()
window.geometry("500x300")
window.title("برنامه ساده من")

language = "fa"

def fa():
    global language
    language = "fa"
    label.config(text="سلام!")
    button.config(text="کلیک کن")
    window.title("برنامه ساده من")

def en():
    global language
    language = "en"
    label.config(text="Hi!")
    button.config(text="Click")
    window.title("My Simple Program")

def de():
    global language
    language = "de"
    label.config(text="Hallo!")
    button.config(text="Klicken")
    window.title("Mein einfaches Programm")

def change_text():
    if language == "fa":
        label.config(text="شما روی دکمه کلیک کردید!")
    elif language == "en":
        label.config(text="You clicked the button!")
    elif language == "de":
        label.config(text="Sie haben auf die Schaltfläche geklickt!")

# ساخت فریم برای دکمه‌ها
frame_buttons = tk.Frame(window)
frame_buttons.grid(row=0, column=0, sticky='w', padx=5, pady=5)

buttonfa = tk.Button(frame_buttons, text="farsi", command=fa)
buttonen = tk.Button(frame_buttons, text="english", command=en)
buttonde = tk.Button(frame_buttons, text="deutsch", command=de)

# دکمه‌ها را داخل فریم افقی بچین (با pack و side=LEFT)
buttonfa.pack(side='left')
buttonen.pack(side='left')
buttonde.pack(side='left')

label = tk.Label(window, text="سلام!", font=("Arial", 14))
label.grid(row=1, column=0, pady=20)

button = tk.Button(window, text="کلیک کن", command=change_text)
button.grid(row=2, column=0)

# ستون 0 وزن بده که بقیه وسط بمونن
window.grid_columnconfigure(0, weight=1)

window.mainloop()

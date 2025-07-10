import tkinter as tk



# ساخت پنجره
window = tk.Tk()
window.title("برنامه ساده من")
window.geometry("500x300")

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

buttonfa = tk.Button(window, text="farsi", command=fa)
buttonen = tk.Button(window, text="english", command=en)
buttonde = tk.Button(window, text="deutsch", command=de)

buttonfa.grid(row=0, column=0, padx=5, pady=5)
buttonen.grid(row=0, column=1, padx=5, pady=5)
buttonde.grid(row=0, column=2, padx=5, pady=5)

label = tk.Label(window, text="سلام!", font=("Arial", 14))
label.grid(row=1, column=0, columnspan=3, pady=20)

button = tk.Button(window, text="کلیک کن", command=change_text)
button.grid(row=2, column=0, columnspan=3)

for i in range(3):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()

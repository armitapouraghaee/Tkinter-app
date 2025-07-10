import tkinter as tk
language = "fa"

# یک پنجره می‌سازیم
window = tk.Tk()
window.title("برنامه ساده من")
window.geometry("500x300")

# لیبل (برچسب)
label = tk.Label(window, text="سلام!", font=("Arial", 14))
label.pack(pady=20)

# تابعی که وقتی دکمه رو بزنی اجرا می‌شه
def change_text():
    if language == "fa":
        label.config(text="شما روی دکمه کلیک کردید!")
    elif language == "en":
        label.config(text="You clicked the button!")
    elif language == "de":
        label.config(text="Sie haben auf die Schaltfläche geklickt!")

# دکمه
button = tk.Button(window, text="کلیک کن", command=change_text)
button.pack()

def en():
    global language
    language = "en"
    label.config(text="Hi!")
    button.config(text="Click")
    window.title("My Simple Program")

#زبان
buttonen = tk.Button(window, text="english", command=en)
buttonen.pack()

def de():
    global language
    language = "de"
    label.config(text="Hallo!")
    button.config(text="Klicken")
    window.title("Mein einfaches Programm")

buttonde = tk.Button(window, text="deutsch", command=de)
buttonde.pack()

# اجرای پنجره
window.mainloop()

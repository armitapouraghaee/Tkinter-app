import tkinter as tk
language = "fa"

# یک پنجره می‌سازیم
window = tk.Tk()
window.title("برنامه ساده من")
window.geometry("300x200")

# لیبل (برچسب)
label = tk.Label(window, text="سلام!", font=("Arial", 14))
label.pack(pady=20)

# تابعی که وقتی دکمه رو بزنی اجرا می‌شه
def change_text():
    if language == "fa":
        label.config(text="شما روی دکمه کلیک کردید!")
    elif language == "en":
        label.config(text="You clicked the button!")

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

# اجرای پنجره
window.mainloop()

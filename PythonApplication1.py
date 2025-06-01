import tkinter as tk

tasks = []

def add_task():
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text=task_text, variable=var, fg=text_color.get(), bg=bg_color.get(), anchor="w")
        checkbox.var = var
        checkbox.pack(fill="x", padx=5, pady=2)
        tasks.append(checkbox)
        entry.delete(0, tk.END)

def apply_theme():
    root.configure(bg=bg_color.get())
    entry.configure(bg="white", fg=text_color.get())
    add_button.configure(bg="lightgray", fg="black")
    frame.configure(bg=bg_color.get())
    for cb in tasks:
        cb.configure(bg=bg_color.get(), fg=text_color.get())

root = tk.Tk()
root.title("To-Do List with Themes")

# انتخاب رنگ‌ها
bg_color = tk.StringVar(value="white")
text_color = tk.StringVar(value="black")

# ورودی تسک
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# دکمه افزودن تسک
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# ناحیه‌ی تسک‌ها
frame = tk.Frame(root)
frame.pack(pady=10)

# منوی رنگ پس‌زمینه
bg_options = ["white", "black", "pink", "yellow", "blue", "green", "orange", "brown", "beige", "purple", "darkgreen", "darkblue"]
tk.Label(root, text="Background Color:").pack()
tk.OptionMenu(root, bg_color, *bg_options).pack()

# منوی رنگ متن
fg_options = ["black", "white", "red", "navy"]
tk.Label(root, text="Text Color:").pack()
tk.OptionMenu(root, text_color, *fg_options).pack()

# دکمه اعمال رنگ‌ها
tk.Button(root, text="Apply Theme", command=apply_theme).pack(pady=10)

root.mainloop()

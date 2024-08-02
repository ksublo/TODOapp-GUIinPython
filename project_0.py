import customtkinter as ctk
from tkcalendar import Calendar
from datetime import datetime, timedelta
from tkinter import Menu
from tkinter import ttk

ctk.set_appearance_mode("Dark")
frames_color = "#ffc0cb"
button_text = "#4f4f4f"
button_fg = "lightblue"
all_text = "#db7093"

root = ctk.CTk()
root.geometry("1000x600")
root.title("TODO list by Kseniia Blokhina")
root.minsize(1000, 600)


#Menu Bar
def open_autor_window():
    new_window = ctk.CTkToplevel(root)
    new_window.geometry("300x100")
    new_window.title("Autor")
    new_window.resizable(False, False)
    new_window.attributes('-topmost', True)
    label1 = ctk.CTkLabel(new_window, text="KSENIIA BLOKHINA (BLO0021)",
                          text_color="pink")
    label1.pack(expand=True)

def open_purpose_window():
    purpose_window = ctk.CTkToplevel(root)
    purpose_window.geometry("500x100")
    purpose_window.title("Purpose")
    purpose_window.resizable(False, False)
    purpose_window.attributes('-topmost', True)

    purpose_text = "This application is designed to help manage your tasks efficiently. You can add, edit, remove, and sort tasks based on various criteria."
    purpose_label = ctk.CTkLabel(purpose_window, text=purpose_text, text_color="pink", wraplength=380)
    purpose_label.pack(pady=20, padx=20)

def set_dark_theme():
    ctk.set_appearance_mode("Dark")

def set_light_theme():
    ctk.set_appearance_mode("Light")


def apply_theme():
    global frames_color, button_text, button_fg

    left_top_frame.configure(fg_color=frames_color)
    left_bottom_frame.configure(fg_color=frames_color)
    right_frame.configure(fg_color=frames_color)

    button.configure(fg_color=button_fg, text_color=button_text)
    add_button.configure(fg_color=button_fg, text_color=button_text)
    today_button.configure(fg_color=button_fg, text_color=button_text)
    week_button.configure(fg_color=button_fg, text_color=button_text)
    all_button.configure(fg_color=button_fg, text_color=button_text)
    done_button.configure(fg_color=button_fg, text_color=button_text)
    remove_button.configure(fg_color=button_fg, text_color=button_text)
    edit_button.configure(fg_color=button_fg, text_color=button_text)
    sort_by_category.configure(fg_color=button_fg, text_color=button_text)

    entry_frame.configure(fg_color=frames_color)
    buttons_frame.configure(fg_color=frames_color)
    edit_frame.configure(fg_color=frames_color)

def change_color_theme(theme):
    global frames_color, button_text, button_fg, all_text
    if theme == "default":
        frames_color = "#ffc0cb"
        button_text = "#4f4f4f"
        button_fg = "lightblue"
    elif theme == "light":
        frames_color = "#ffffff"
        button_text = "#000000"
        button_fg = "#cccccc"
    elif theme == "dark":
        frames_color = "#333333"
        button_text = "#ffffff"
        button_fg = "#555555"
    apply_theme()


menubar = Menu(root)
root.config(menu=menubar)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear")
edit_menu.add_command(label="Save")
edit_menu.add_separator()
edit_menu.add_command(label="Exit", command=root.quit)

view_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)
theme_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Dark", command=set_dark_theme)
theme_menu.add_command(label="Light", command=set_light_theme)
colors_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Colors", menu=colors_menu)
colors_menu.add_command(label="Default", command=lambda: change_color_theme("default"))
colors_menu.add_command(label="Light", command=lambda: change_color_theme("light"))
colors_menu.add_command(label="Dark", command=lambda: change_color_theme("dark"))


autor_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Info", menu=autor_menu)
autor_menu.add_command(label="Purpose", command=open_purpose_window)
autor_menu.add_command(label="Autor", command=open_autor_window)

#GRID FRAMES
left_top_frame = ctk.CTkScrollableFrame(root, fg_color=frames_color)
left_bottom_frame = ctk.CTkFrame(root, fg_color=frames_color)
right_frame = ctk.CTkFrame(root, fg_color=frames_color)

left_top_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=(20, 10))
left_bottom_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=(10, 20))
right_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(10, 20), pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

#LEFT BOTTOM FRAME
top_frame_label = ctk.CTkLabel(left_bottom_frame, text="CALCULATE DAYS",
                               font=("Candara", 20), text_color=all_text)
top_frame_label.pack(pady=(20, 0))

cal = Calendar(left_bottom_frame,
               background='white', foreground='black', bordercolor='pink',
               headersbackground='pink', headersforeground='black',
               selectbackground='gray', selectforeground='white',
               normalbackground='white', normalforeground='black',
               weekendbackground='white', weekendforeground='black',
               othermonthforeground='black', othermonthbackground='lightgray',
               othermonthweforeground='black', othermonthwebackground='lightgray')
cal.pack(pady=(20, 0), padx=20)


def calculate_days():
    selected_date_str = cal.get_date()
    selected_date = datetime.strptime(selected_date_str, '%m/%d/%y').date()
    current_date = datetime.now().date()
    delta = selected_date - current_date

    date_entry.delete(0, "end")
    date_entry.insert(0, selected_date.strftime('%d-%m-%Y'))

    if delta.days > 0:
        date.configure(text=f"Days left: {delta.days}")
    elif delta.days < 0:
        date.configure(text="Passed")
    else:
        date.configure(text="It's today!")


date = ctk.CTkLabel(left_bottom_frame, text="Days left: ",
                    text_color=all_text, padx=20, pady=5, font=("Candara", 14))
date.pack(pady=(10, 0))

button = ctk.CTkButton(left_bottom_frame, text="GET DATE", command=calculate_days,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
button.pack(pady=10)

#LEFT TOP FRAME
top_frame_label = ctk.CTkLabel(left_top_frame, text="ADD YOUR 'TODO' ",
                               font=("Candara", 20), text_color=all_text)
top_frame_label.pack(pady=(20, 10))

entry_frame = ctk.CTkFrame(left_top_frame, fg_color=frames_color)
entry_frame.pack(padx=(5, 5), pady=(5, 5))

todo_label = ctk.CTkLabel(entry_frame, text="To-Do:", text_color=all_text, font=("Candara", 14))
todo_entry = ctk.CTkEntry(entry_frame, fg_color="white", border_color=all_text,
                          text_color=all_text, placeholder_text="task",
                          placeholder_text_color="lightgray")

notes_label = ctk.CTkLabel(entry_frame, text="Note:", text_color=all_text, font=("Candara", 14))
notes_entry = ctk.CTkEntry(entry_frame, fg_color="white", border_color=all_text,
                           text_color=all_text, placeholder_text="your notes",
                           placeholder_text_color="lightgray")

date_label = ctk.CTkLabel(entry_frame, text="Date:", text_color=all_text, font=("Candara", 14))
date_entry = ctk.CTkEntry(entry_frame, fg_color="white", border_color=all_text,
                          text_color=all_text, placeholder_text="00-00-0000",
                          placeholder_text_color="lightgray")

todo_label.grid(row=0, column=0, padx=10, pady=(0, 0), sticky='w')
date_label.grid(row=2, column=0, padx=10, pady=(0, 0), sticky='w')
notes_label.grid(row=0, column=1, padx=10, pady=(0, 0), sticky='w')

entry_frame.grid_rowconfigure(1, weight=1)
todo_entry.grid(row=1, column=0, padx=10, pady=0, sticky='ew')
date_entry.grid(row=3, column=0, padx=10, pady=0, sticky='ew')
notes_entry.grid(row=1, column=1, rowspan=3, padx=10, pady=0, sticky='nsew')

entry_frame.grid_columnconfigure(0, weight=1)
entry_frame.grid_columnconfigure(1, weight=1)

edit_frame = ctk.CTkFrame(left_top_frame, fg_color=frames_color)
edit_frame.pack(padx=10, pady=(10, 20))

edit_label = ctk.CTkLabel(edit_frame, text="🔽 TASK PROPERTIES 🔽",
                               font=("Candara", 20), text_color=all_text)
edit_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

hardness_label = ctk.CTkLabel(edit_frame, text="Hardness Assessment:", font=("Candara", 14), text_color=all_text)
hardness_label.grid(row=1, column=0, sticky="w", padx=0, pady=(2, 0))
hardness_slider = ctk.CTkSlider(master=edit_frame, from_=0, to=10,
                                button_color=all_text, progress_color="white")
hardness_slider.grid(row=2, column=0, sticky="w", padx=0, pady=(0, 2))

readiness_label = ctk.CTkLabel(edit_frame, text="Percent of Readiness:", font=("Candara", 14), text_color=all_text)
readiness_label.grid(row=3, column=0, sticky="w", padx=0, pady=(2, 0))
readiness_slider = ctk.CTkSlider(master=edit_frame, from_=0, to=100,
                                 button_color=all_text, progress_color="white")
readiness_slider.grid(row=4, column=0, sticky="w", padx=0, pady=(0, 2))

edit_frame.grid_columnconfigure(0, weight=1)
edit_frame.grid_columnconfigure(1, weight=1)

category_label = ctk.CTkLabel(edit_frame, text="Category:", font=("Candara", 14), text_color=all_text)
category_label.grid(row=2, column=1, sticky="w", padx=10, pady=2)
category_var = ctk.StringVar(value="Select a category")
categories = ["School", "Home", "Work", "Personal"]
category_option_menu = ctk.CTkOptionMenu(edit_frame, variable=category_var, values=categories,
                                         fg_color=all_text, button_color=all_text,
                                         dropdown_fg_color="white", dropdown_text_color=all_text)
category_option_menu.grid(row=3, column=1, sticky="w", padx=10, pady=2)


def insert_todo():  #ADD TASK FUNCTION
    todo_text = todo_entry.get()
    notes_text = notes_entry.get()
    date_text = date_entry.get()
    hardness_value = round(hardness_slider.get(), 1)
    readiness_value = round(readiness_slider.get(), 1)
    category_value = category_var.get()

    if not todo_text and not date_text:
        return

    task_number = len(treeview1.get_children()) + 1
    treeview1.insert('', 'end', text=str(task_number),
                     values=(todo_text, notes_text, date_text, hardness_value, readiness_value, category_value))

    todo_entry.delete(0, 'end')
    notes_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    hardness_slider.set(0)
    readiness_slider.set(0)
    category_var.set("Select a category")


add_button = ctk.CTkButton(left_top_frame, text="ADD", command=insert_todo,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
add_button.pack(pady=(20, 10))


#RIGHT FRAME
top_frame_label = ctk.CTkLabel(right_frame, text="YOUR TODO LIST ",
                               font=("Candara", 20), text_color=all_text)
top_frame_label.pack(pady=(20, 10), padx=0)

style = ttk.Style()
style.configure('TNotebook', padding=(5, 5),
                foreground=all_text, background="white",
                font=('Candara', 20))

notebook_frame = ctk.CTkFrame(right_frame)
notebook_frame.pack()

notebook = ttk.Notebook(notebook_frame, style="TNotebook")
notebook.pack()

style.configure("Treeview",
                background="whitr",
                fieldbackground="pink",
                foreground=all_text,
                font=('Candara', 14))

style.configure("Treeview.Heading",
                background="blue",
                foreground=all_text,
                font=('Candara', 16))

style.map("Treeview",
          background=[('selected', 'lightblue')],
          foreground=[('selected', '#ffffff')])

#actual
tab1 = ctk.CTkFrame(notebook)
notebook.add(tab1, text='ACTUAL')

treeview1 = ttk.Treeview(tab1)

treeview1['columns'] = ("1", "2", "3", "4", "5", "6")

treeview1.column("#0", width=30, anchor='w')
treeview1.column("1", width=100, anchor='w')
treeview1.column("2", width=150, anchor='w')
treeview1.column("3", width=100, anchor='w')
treeview1.column("4", width=55, anchor='w')
treeview1.column("5", width=65, anchor='w')
treeview1.column("6", width=100, anchor='w')

treeview1.heading("#0", text="N", anchor='w')
treeview1.heading("1", text="TODO", anchor='w')
treeview1.heading("2", text="Notes", anchor='w')
treeview1.heading("3", text="Date", anchor="w")
treeview1.heading("4", text="Hard", anchor='w')
treeview1.heading("5", text="Ready", anchor='w')
treeview1.heading("6", text="Category", anchor='w')

treeview1.pack(expand=True, fill='both')

#done
tab2 = ctk.CTkFrame(notebook)
notebook.add(tab2, text='DONE')

treeview2 = ttk.Treeview(tab2)

treeview2['columns'] = ("1", "2", "3", "4", "5")


treeview2.column("#0", width=2, anchor='w')
treeview2.column("1", width=150, anchor='w')
treeview2.column("2", width=100, anchor='w')
treeview2.column("3", width=150, anchor='w')
treeview2.column("4", width=150, anchor='w')
treeview2.column("5", width=150, anchor='w')

treeview2.heading("#0", text="", anchor='w')
treeview2.heading("1", text="TODO", anchor='w')
treeview2.heading("2", text="Notes", anchor='w')
treeview2.heading("3", text="Date", anchor="w")
treeview2.heading("4", text="Success", anchor="w")
treeview2.heading("5", text="Review", anchor="w")



treeview2.pack(expand=True, fill='both')

notebook_frame.pack()
notebook.pack(expand=True, fill='both')

#buttons
buttons_frame = ctk.CTkFrame(right_frame, fg_color=frames_color)
buttons_frame.pack(padx=10, pady=(40, 0))

edits_label = ctk.CTkLabel(buttons_frame, text="EDITS",
                               font=("Candara", 16), text_color=all_text)
edits_label.grid(column=0, row=0, sticky="ew")

sort_label = ctk.CTkLabel(buttons_frame, text="SORTING",
                               font=("Candara", 16), text_color=all_text)
sort_label.grid(column=1, row=0, sticky="ew")


def show_todos_for_today():
    today = datetime.now().strftime('%d-%m-%Y')

    for item in treeview1.get_children():
        item_date = treeview1.item(item, 'values')[2]
        if item_date == today:
            treeview1.item(item, tags=('visible',))
        else:
            treeview1.item(item, tags=('hidden',))

    treeview1.tag_configure('visible', foreground='#db7093')
    treeview1.tag_configure('hidden', foreground='#f0f0f0')

today_button = ctk.CTkButton(buttons_frame, text="THIS DAY", command=show_todos_for_today,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
today_button.grid(row=1, column=1, sticky="e", padx=10, pady=2)


def show_todos_for_this_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    for item in treeview1.get_children():
        item_date_str = treeview1.item(item, 'values')[2]
        try:
            item_date = datetime.strptime(item_date_str, '%d-%m-%Y')
        except ValueError:
            continue

        if start_of_week <= item_date <= end_of_week:
            treeview1.item(item, tags=('visible',))
        else:
            treeview1.item(item, tags=('hidden',))

    treeview1.tag_configure('visible', foreground='#db7093')
    treeview1.tag_configure('hidden', foreground='#f0f0f0')

week_button = ctk.CTkButton(buttons_frame, text="THIS WEEK", command=show_todos_for_this_week,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
week_button.grid(row=2, column=1, sticky="e", padx=10, pady=2)

def show_all_todos():
    for item in treeview1.get_children():
        treeview1.item(item, tags=('visible',))

    treeview1.tag_configure('visible', foreground='#db7093')

all_button = ctk.CTkButton(buttons_frame, text="ALL TODOs", command=show_all_todos,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
all_button.grid(row=3, column=1, sticky="e", padx=10, pady=2)

def mark_as_done():
    selected_item = treeview1.selection()
    if not selected_item:
        print("No item selected")
        return

    done_window = ctk.CTkToplevel(root)
    done_window.title("Task Completion")
    done_window.geometry("300x230")
    done_window.resizable(False, False)
    done_window.attributes('-topmost', True)

    success_label = ctk.CTkLabel(done_window, text="Success Level:",
                                 font=("Candara", 14), text_color=all_text)
    success_label.pack(pady=(10, 0))

    success_entry = ctk.CTkEntry(done_window, fg_color="white",
                                 border_color=all_text, text_color=all_text)
    success_entry.pack(pady=2)

    review_label = ctk.CTkLabel(done_window, text="Review Notes:",
                                font=("Candara", 14), text_color=all_text)
    review_label.pack(pady=(10, 0))

    review_entry = ctk.CTkEntry(done_window, fg_color="white",
                                border_color=all_text, text_color=all_text)
    review_entry.pack(pady=(0, 10))

    def end_task():
        success_text = success_entry.get()
        review_text = review_entry.get()
        item_values = treeview1.item(selected_item, 'values')
        treeview2.insert('', 'end', values=(item_values[0], item_values[1],
                                            item_values[2], success_text, review_text))
        treeview1.delete(selected_item)
        done_window.destroy()

    end_button = ctk.CTkButton(done_window, text="END TASK", command=end_task, fg_color=button_fg, text_color=button_text, hover_color="lightgray", font=("Candara", 16))
    end_button.pack(pady=20)


done_button = ctk.CTkButton(buttons_frame, text="DONE", command=mark_as_done,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
done_button.grid(row=1, column=0, sticky="w", padx=10, pady=2)

def remove_todo():
    selected_item = treeview1.selection()
    if selected_item:
        selected_item = treeview1.selection()
        treeview1.delete(selected_item)
    else:
        print("No item selected")


remove_button = ctk.CTkButton(buttons_frame, text="REMOVE", command=remove_todo,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
remove_button.grid(row=2, column=0, sticky="w", padx=10, pady=2)

def edit():
    selected_item = treeview1.selection()
    if selected_item:
        item_values = treeview1.item(selected_item, 'values')

        todo_entry.delete(0, 'end')
        todo_entry.insert(0, item_values[0])

        notes_entry.delete(0, 'end')
        notes_entry.insert(0, item_values[1])

        date_entry.delete(0, 'end')
        date_entry.insert(0, item_values[2])

        try:
            hardness_value = float(item_values[3])
            readiness_value = float(item_values[4])
        except ValueError:
            hardness_value = 0
            readiness_value = 0

        hardness_slider.set(hardness_value)
        readiness_slider.set(readiness_value)
        category_var.set(item_values[5])

        add_button.configure(text="UPDATE", command=lambda: update_item(selected_item))

def update_item(selected_item):
    # Capture the updated values
    updated_todo = todo_entry.get()
    updated_notes = notes_entry.get()
    updated_date = date_entry.get()
    updated_hardness = round(hardness_slider.get(), 1)
    updated_readiness = round(readiness_slider.get(), 1)
    updated_category = category_var.get()

    treeview1.item(selected_item, values=(updated_todo, updated_notes, updated_date,
                                          updated_hardness, updated_readiness, updated_category))

    todo_entry.delete(0, 'end')
    notes_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    hardness_slider.set(0)
    readiness_slider.set(0)
    category_var.set("Select a category")
    add_button.configure(text="ADD", command=insert_todo)


edit_button = ctk.CTkButton(buttons_frame, text="EDIT", command=edit,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
edit_button.grid(row=3, column=0, sticky="w", padx=10, pady=2)

def sort_items_by_category():
    selected_category = category_varr.get()
    if selected_category == "Select a category":
        print("Please select a category to sort.")
        return
    for item in treeview1.get_children():
        item_values = treeview1.item(item, 'values')
        item_category = item_values[5] if len(item_values) > 5 else ''

        if item_category == selected_category:
            treeview1.item(item, tags=('visible',))
        else:
            treeview1.item(item, tags=('hidden',))

    treeview1.tag_configure('visible', foreground='#db7093')
    treeview1.tag_configure('hidden', foreground='#f0f0f0')


category_label = ctk.CTkLabel(buttons_frame, text="CATEGORY SORT", font=("Candara", 16), text_color=all_text)
category_label.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 2))
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)

category_varr = ctk.StringVar(value="Select a category")
categories = ["School", "Home", "Work", "Personal"]
category_option_menu = ctk.CTkOptionMenu(buttons_frame, variable=category_varr, values=categories,
                                         fg_color=all_text, button_color=all_text,
                                         dropdown_fg_color="white", dropdown_text_color=all_text)
category_option_menu.grid(row=5, column=0, sticky="w", padx=10, pady=2)

sort_by_category = ctk.CTkButton(buttons_frame, text="SORT CATEGORY", command=sort_items_by_category,
                       fg_color=button_fg, text_color=button_text, hover_color="lightgray",
                       font=("Candara", 16))
sort_by_category.grid(row=5, column=1, sticky="w", padx=10, pady=2)


treeview1.insert('', 'end', text=str(1),
                     values=("URO", "project", "20-03-2024",
                             80, 99, "School"))

treeview1.insert('', 'end', text=str(1),
                     values=("Visa", "make a visa", "24-07-2024",
                             0, 30, "Personal"))

treeview1.insert('', 'end', text=str(1),
                     values=("JAVA", "du2", "20-03-2024",
                             40, 20, "School"))

treeview1.insert('', 'end', text=str(1),
                     values=("DS", "cv3-5", "21-03-2024",
                             50, 10, "School"))

root.mainloop()

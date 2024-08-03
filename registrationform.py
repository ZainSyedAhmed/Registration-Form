import tkinter as tk

form = tk.Tk()
form.geometry("500x600")
form.title("Registration Form")
form.configure(bg="black")

name_label = tk.Label(form, text="Full name", bg="black", fg="white")
name_label.pack(pady=(10, 0))
name_textbox = tk.Entry(form)
name_textbox.pack(pady=5)

email_label = tk.Label(form, text="Email", bg="black", fg="white")
email_label.pack(pady=(10, 0))
email_textbox = tk.Entry(form)
email_textbox.pack(pady=5)

gender_frame = tk.Frame(form, bg="black")
gender_frame.pack(pady=20) 

gender_label = tk.Label(gender_frame, text="Gender", bg="black", fg="white")
gender_label.pack()

v = tk.IntVar()
tk.Radiobutton(gender_frame, text="Male", padx=20, variable=v, value=1, bg="black", fg="white").pack(anchor=tk.W)
tk.Radiobutton(gender_frame, text="Female", padx=20, variable=v, value=2, bg="black", fg="white").pack(anchor=tk.W)

country_label = tk.Label(form, text="Country", bg="black", fg="white")
country_label.pack(pady=(10, 0))
country_listbox = tk.Listbox(form, width=30)
countries = ["Pakistan", "Bahrain", "Dubai", "Saudi Arabia","Singapore","Turkey","Oman"]
for country in countries:
    country_listbox.insert(tk.END, country)
country_listbox.pack(pady=5)
country_listbox.select_set(0)

programming_frame = tk.Frame(form, bg="black")
programming_frame.pack(pady=20)

tk.Label(programming_frame, text="Programming Languages", bg="black", fg="white").pack(pady=10)

var1 = tk.IntVar()
check1 = tk.Checkbutton(programming_frame, text="Java", variable=var1, bg="black", fg="white")
check1.select()
check1.pack()

var2 = tk.IntVar()
check2 = tk.Checkbutton(programming_frame, text="Python", variable=var2, bg="black", fg="white")
check2.deselect()
check2.pack()

submit_button = tk.Button(form, text='Submit', bg="blue", fg="blue")
submit_button.pack(pady=20)

form.mainloop()
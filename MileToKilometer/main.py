from tkinter import Tk, Label, Entry, Button

def converter():
	miles = float(miles_entry.get())
	result_label.config(text=f"{round(miles * 1.6093, 2)}")

window = Tk()
window.title("Miles To Kilometers Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

Km_label = Label(text="Km")
Km_label.grid(row=1, column=2)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

calculate_button = Button(text="Calculate")
calculate_button.grid(row=2, column=1)
calculate_button.config(command=converter)

window.mainloop()
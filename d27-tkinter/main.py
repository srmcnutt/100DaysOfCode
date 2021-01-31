import tkinter

FONT = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("Miles to Kilometer Calulator")
window.minsize(height=100, width=200)
window.configure(padx=20, pady=20)

def button_clicked(text="I got clicked"):
    print(text)
    km = round(float(input.get()) * 1.609, 2)
    label_result.config(text=km)


# label
label_is_equal_to = tkinter.Label(text="is equal to", font=FONT)
label_is_equal_to.grid(column=0,row=1)

#entry
input = tkinter.Entry()
input.config(width=5)
input.grid(column=1,row=0)

# label
result = 0
label_result = tkinter.Label(text=result, font=FONT)
label_result.grid(column=1,row=1)

#button
button = tkinter.Button(text="calculate", command=button_clicked)
button.grid(column=1,row=2)

# label
result = 0
label_miles = tkinter.Label(text="Miles", font=FONT)
label_miles.grid(column=2,row=0)

# label
result = 0
label_km = tkinter.Label(text="Km", font=FONT)
label_km.grid(column=2,row=1)



window.mainloop()
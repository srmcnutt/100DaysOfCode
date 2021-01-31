import tkinter

FONT = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(height=300, width=500)

def button_clicked(text="I got clicked"):
    print(text)
    new_text = input.get()
    my_label.config(text=new_text)


# label
label_is_equal_to = tkinter.Label(text="is equal to", font=FONT)
label_is_equal_to.grid(column=0,row=1)

#entry
input = tkinter.Entry()
input.grid(column=1,row=0)

#button
button = tkinter.Button(text="calculate", command=button_clicked)
button.grid(column=1,row=1)




window.mainloop()
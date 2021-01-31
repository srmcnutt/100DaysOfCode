import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(height=300, width=500)

def button_clicked(text="I got clicked"):
    print(text)
    new_text = input.get()
    my_label.config(text=new_text)


# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

#button
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)

#button
new_button = tkinter.Button(text="new_button", command=button_clicked)
new_button.grid(column=2,row=0)

#entry
input = tkinter.Entry()
input.grid(column=3,row=2)

window.mainloop()
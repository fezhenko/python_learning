from tkinter import *

# create a window
window = Tk()


def kg_to_grams_pounds_ounces():
    print('Success!')
    grams = int(e1_value.get()) * 1000
    pounds = int(e1_value.get()) * 2.20462
    ounces = int(e1_value.get()) * 35.274
    t1.delete('1.0', END) # Deletes the content of the Text box from start to END
    t1.insert(END, grams)
    t2.delete('1.0', END)
    t2.insert(END, pounds)
    t3.delete('1.0', END)
    t3.insert(END, ounces)


lbl = Label(window, text='Kg')
lbl.grid(row=0, column=0)

# create button
btn = Button(window, text='Convert', command=kg_to_grams_pounds_ounces)
btn.grid(row=0, column=2)

# Entry - Пользовательский ввод
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# fields that will be filled by results
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)




# This makes sure to keep the main window open
window.mainloop()

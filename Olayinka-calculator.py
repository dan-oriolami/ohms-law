from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END
import tkinter.messagebox

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title(" Ola's Calculator")
        self.geometry("300x400")

        # Title label
        self.title_label = Label(self, text="Simple Calculator 😊")
        self.title_label.pack()

        # Entry widget
        self.entry = Entry(self, width=30)
        self.entry.insert(0, "1+2")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.onclick())

        # Result label
        self.label = Label(self, text="")
        self.label.pack()

        # Compute button
        self.button = Button(self, text="Compute", command=self.onclick)
        self.button.pack(pady=5)

        # Clear button
        self.clear_button = Button(self, text="Clear", command=self.clear)
        self.clear_button.pack(pady=5)

        # History log
        self.history_label = Label(self, text="History:")
        self.history_label.pack()

        self.history_box = Text(self, height=8, width=35)
        self.history_box.pack()

        self.scrollbar = Scrollbar(self, command=self.history_box.yview)
        self.history_box.config(yscrollcommand=self.scrollbar.set)

    def onclick(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.label.configure(text=f"= {result}")
            self.history_box.insert(END, f"{expression} = {result}\n")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Invalid input:\n{e}")
            self.label.configure(text="")

    def clear(self):
        self.entry.delete(0, END)
        self.label.configure(text="")

root = Root()
root.mainloop()

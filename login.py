# create user login file
# create function to verify if user qualifies
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("500x200")
root.title("Thuba Lotto")
root.configure(bg="IndianRed")


def check():
    age = int(entry1.get())
    if age < 18:
        messagebox.showinfo("Checks", "You Don't Qualify")
    else:
        messagebox.showinfo("Success", "Go through!")
        root.withdraw()
        import lotto


label1 = Label(root, bg="grey20", text="Enter Your Age", width=500, fg="white", font="Roboto 15")
label1.pack()
empty_label = Label(root, width=5, bg="IndianRed")
empty_label.pack()
entry1 = Entry(root, width=10, font="Roboto 20")
entry1.pack()
empty_label = Label(root, width=5, bg="IndianRed")
empty_label.pack()
btn1 = Button(root, text="SUBMIT", bg="grey20", fg="white", width="30", height="3", font="Roboto 10", command=check)
btn1.pack()
root.mainloop()

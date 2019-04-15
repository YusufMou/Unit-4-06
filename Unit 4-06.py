from tkinter import *

root = Tk()
root.title("String comparator")
root.geometry("500x300")

Label(root, text="This is a string convertor").grid(row=1, column=1)
Label(root, text="Enter both the sentences below").grid(row=2, column=1)

e1 = Entry(root)
e1.grid(row=3, column=1)
e2 = Entry(root)
e2.grid(row=4, column=1)

def comparison():
	sent1 = str(e1.get())
	sent2 = str(e2.get())
	if sent1 == sent2:
		match = Label(root, text="The sentences match").grid(row=6, column=1)
	else:
		dmatch = Label(root, text="The sentences don't match").grid(row=6, column=1)

comp = Button()			
comp ["text"] = "Compare"
comp ["command"] = comparison
comp.grid(row=5, column=1)



root.mainloop()
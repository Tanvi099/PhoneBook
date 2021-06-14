from Tkinter import *
root=Tk()
root.geometry('1050x1050')
Label(root,text="Project title: Phonebook",relief='ridge',font=("Arial 20"),bg='yellow').grid(row=0,column=0)
Label(root,text="Project of Python and Database",font=("Arial 18"),fg="red").grid(row=1,column=1)
Label(root,text="Developed by: Tanvi Sharma",font=("Arial 18"),fg="Blue").grid(row=2,column=1)

def close1(e=1):
    root.destroy()
root.bind('<Motion>',close1)
root.mainloop()

from tkinter import *

root=Tk()
root.geometry("500x300")
root.title('Guess The Number')
Label(root, text='Website-Blocker', font='arial 20 bold').pack()
Label(root, text=':- an3rdone', font='arial 10 ').pack()


websites=StringVar()
websites=str(websites)
Label(root, text='Enter Url of Website', font='arial 15 bold ').place(relx=0.4,rely=0.3,anchor=CENTER)
e1=Entry(root,textvariable=websites,width=50).place(relx=0.2,rely=0.4)

host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
def block():
    try:
        with open(host_path,"r+") as fptr:
                content=fptr.read()

                if websites in content:
                            pass
                else:
                            fptr.write(redirect + "        " + websites + "\n")
        Label(root, text='blocked successfully', font='arial 10 bold ').place(relx=0.5, rely=0.8, anchor=CENTER)
    except:
        Label(root, text='failed', font='arial 10 bold ').place(relx=0.5, rely=0.8, anchor=CENTER)
block = Button(root, text='BLOCK', width=20, command=block,
                 bg="red", activebackground="red", relief=GROOVE)
block.place(relx=0.5, rely=0.6, anchor=S)
root.mainloop()


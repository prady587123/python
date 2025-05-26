from tkinter import*
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

num = [
    [9,8,7],
    [6,5,4],
    [3,2,1],
    ['#',0,'*']
]

for i in range(4):
    root.rowconfigure(i,weight=1,minsize=50)
for j in range(3):
    root.columnconfigure(j , weight=1, minsize =75)
    for j in range(3):
        root.columnconfigure(j,weight=1,minsize=75)
for i in range(4):
    for j in range(3):
        frame = Frame(master=root,reliefe=SUNKEN,borderwidth=1)
        frame.grid(row=i,colum=j , sticky=SUNKEN, borderwidth=1)
        label = Label(master=frame, text=num[i][j],bg = '#d0efff',font=('Arial',16))
        label.pack(expand=True,fill='both')
        root.mainloop()
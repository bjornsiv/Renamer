import os;
from tkinter import N, ttk, Tk, Entry, Label, filedialog as fd
window = Tk()
window.title("Rename files")
window.geometry('300x200')

Label_top = Label(window, text="Rename your files")
Label_top.grid(column=1, row=0)

User_fileName = Entry(window)
User_fileName.grid(column=1, row=1)
Label_fileName = Label(window, text = "FilenName:")
Label_fileName.grid(column=0, row=1)

User_fileExt = Entry(window)
User_fileExt.grid(column=1, row=2)
Label_fileName = Label(window, text = "FileExtension:")
Label_fileName.grid(column=0, row=2)

User_filePath = Entry(window)
User_filePath.grid(column=1, row=3)
Label_fileName = Label(window, text = "FilePath:")
Label_fileName.grid(column=0, row=3)

def printInput():
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    count = 1
    dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
    print("FileName: " + inp + "\n" + "FileExt: " + inp2 + "\n" + "FinalFileName: " + dst)

def rename():
    folder = "Files"
    inp = User_fileName.get()
    inp2 = User_fileExt.get()

    for count, filename in enumerate(os.listdir(folder), 1):
        dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
        src =f"{folder}/{filename}" 
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

renameButton = ttk.Button(window,text = "Rename", command = rename)
renameButton.grid(column=1)
printButton = ttk.Button(window,text = "Print", command = printInput)
printButton.grid(column=1)
exit_button = ttk.Button(window,text='Exit',command=lambda: window.quit())
exit_button.grid(column=1)
window.mainloop()
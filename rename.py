import os;
from tkinter import ttk, Tk, Entry, Label, filedialog as fd
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

User_filePath = Entry(window) #state=DISABLED
User_filePath.grid(column=1, row=3)
Label_fileName = Label(window, text = "FilePath:")
Label_fileName.grid(column=0, row=3)


folder = "Files"
initDir = f"{str(os.getcwd())}/{folder}"
User_filePath.insert(0, initDir)

def printInput():
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    count = 1
    dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
    print(f"FileName: {inp}\nFileExt: {inp2}\nFinalFileName: {dst}")

def rename():
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    totalFiles = len(os.listdir(User_filePath.get()))

    print(f"Starting Renaming")
    for count, filename in enumerate(os.listdir(User_filePath.get()), 1):
        dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
        src =f"{User_filePath.get()}/{filename}" 
        dst =f"{User_filePath.get()}/{dst}"
        os.rename(src, dst)
        print(f"Renaming {count} of {totalFiles}")

def findPath():
    f = fd.askdirectory(initialdir=initDir)
    print("File Path: " + f)
    User_filePath.delete(0, 'end')
    User_filePath.insert(0, f)


renameButton = ttk.Button(window,text = "Rename", command = rename)
renameButton.grid(column=0, row=4)
pathButton = ttk.Button(window,text = "Path", command = findPath)
pathButton.grid(column=0, row=5)
printButton = ttk.Button(window,text = "Print", command = printInput)
printButton.grid(column=1, row=4)
exit_button = ttk.Button(window,text='Exit',command=lambda: window.quit())
exit_button.grid(column=1, row=5)
window.mainloop()
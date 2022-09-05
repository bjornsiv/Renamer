import os;

from tkinter import N, ttk, Tk, Entry
window = Tk()
window.title("Rename files")
window.geometry('200x150')
User_fileName = Entry()
User_fileName.pack()
User_fileExt = Entry()
User_fileExt.pack()

def printInput():
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    count = 1
    dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
    print("FileName: " + inp + "\n" + "FileExt: " + inp2 + "\n" + "FinalFileName: " + dst)

fileName = str(User_fileName.get()) #"The Bad Batch - S01E"
fileExt = str(User_fileExt.get())#".mkv"



def rename():
    folder = "Files"
    cwd = os.getcwd()
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    #folderName = os.path.join(cwd, folder)    
    #print(os.listdir(folderName))
    #print(cwd, folderName)
    #count = 1; 
    for count, filename in enumerate(os.listdir(folder), 1):
        dst = f"{str(inp) + str(count).zfill(2) + str(inp2)}"
        src =f"{folder}/{filename}" 
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

renameButton = ttk.Button(window,text = "Rename", command = rename)
renameButton.pack()
printButton = ttk.Button(window,text = "Print", command = printInput)
printButton.pack()
exit_button = ttk.Button(window,text='Exit',command=lambda: window.quit())
exit_button.pack()
window.mainloop()
import os;

from tkinter import ttk, Tk, Entry
window = Tk()
window.title("Rename files")
window.geometry('200x100')
User_input = Entry()
User_input.pack()

def printInput():
    inp = User_input.get()
    print(inp)


fileName = str(User_input.get()) #"The Bad Batch - S01E"
fileExt = ".mkv"







def rename():
    folder = "Files"
    cwd = os.getcwd()
    folderName = os.path.join(cwd, folder)    
    
    print(os.listdir(folderName))
    print(cwd, folderName)

    count = 1; 
    for count, filename in enumerate(os.listdir(folder), 1):
        dst = f"{str(fileName) + str(count) + str(fileExt)}"
        src =f"{folder}/{filename}" 
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

renameButton = ttk.Button(window,text = "Rename", command = printInput)
renameButton.pack()
exit_button = ttk.Button(window,text='Exit',command=lambda: window.quit())
exit_button.pack()
window.mainloop()
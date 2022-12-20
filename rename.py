import os;
from tkinter import ttk, Tk, IntVar, Entry, Label, filedialog as fd;
import datetime;


window = Tk()
window.title("Rename files")
window.geometry('350x200')
todaysDate = datetime.datetime.now()
yearCheck = IntVar(window, False)
monthCheck = IntVar(window, False)
dayCheck = IntVar(window, False)

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
    inpDate = ""
    if yearCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.strftime("%y"))
    if monthCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.month)
    if dayCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.day)


    print(f"YearCheck: {yearCheck.get()}\nMonthCheck: {monthCheck.get()}\nDayCheck: {dayCheck.get()}")
    print(f"Year: {todaysDate.year}\nMonth: {todaysDate.month}\nDay: {todaysDate.day}\n\n{inpDate}")
    

    dst = f"{str(inp) + str(inpDate) + str(count).zfill(2) + str(inp2)}"
    print(f"FileName: {inp}\nFileExt: {inp2}\nFinalFileName: {dst}")
    

def rename():
    inp = User_fileName.get()
    inp2 = User_fileExt.get()
    totalFiles = len(os.listdir(User_filePath.get()))
    inpDate = ""
    if yearCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.strftime("%y"))
    if monthCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.month)
    if dayCheck.get() == 1:
        inpDate = inpDate + str(todaysDate.day)
    
    print(f"Starting Renaming")
    for count, filename in enumerate(os.listdir(User_filePath.get()), 1):
        dst = f"{str(inp) + str(inpDate) + str(count).zfill(2) + str(inp2)}"
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
yearRadio = ttk.Checkbutton(window, text = "Year", variable = yearCheck, onvalue = 1, offvalue = 0)
yearRadio.grid(column=2, row=4)
monthRadio = ttk.Checkbutton(window, text = "Month", variable = monthCheck, onvalue = 1, offvalue = 0)
monthRadio.grid(column=2, row=5)
dayRadio = ttk.Checkbutton(window, text = "Day", variable = dayCheck, onvalue = 1, offvalue = 0)
dayRadio.grid(column=2, row=6)
window.mainloop()
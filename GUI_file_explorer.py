from tkinter import *
from os_ops import get_list_of_files
from merge_pdf import pdf_op
from tkinter import messagebox
import os
import logging as lg
lg.basicConfig(filename='gui_logs.log',level=lg.INFO,format="%(asctime)s:%(levelname)s: %(message)s")

root = Tk()
root.title("File_Explorer")

label_header = Label(root,text="Please enter the directory path below:")
label_header.grid(row=0,column=0)

e = Entry(root,width=100,borderwidth=5)
e.grid(row=1,column=0,columnspan=10)

def os_func():
    dir = e.get()
    obj = get_list_of_files(dir)
    itr = obj.show_list()
    count = 0
    box = Listbox(root,width=100, height=40)
    box.grid(row=3, column=0)
    while True:
        try:
            box.insert(END,itr[count])

            #temp_label = Label(root,text=itr[count])
            #temp_label.grid(row=3+count,column=0)
            count +=1
        except StopIteration:
            break

def clear_func():
    e.delete(0,END)

clicked = StringVar(root)
clicked.set("List files")
drop = OptionMenu(root,clicked,"List files","Merge_pdf_files")
drop.grid(row=3,column=13)



def custom_command():
    file_list = []
    option = clicked.get()
    if option == "List files":

        dir = e.get()
        obj = get_list_of_files(dir)
        file_list = obj.get_list()
        count = 0
        box = Listbox(root, width=100, height=40)
        box.grid(row=4, column=0)
        while True:
            try:
                box.insert(END, file_list[count])
                count += 1
            except IndexError:
                break
    else:
        try:
            dir = e.get()
            obj = get_list_of_files(dir)
            file_list = obj.get_list()
            os.chdir(dir)
            pd = pdf_op()
            pdf_files = pd.get_pdfs(file_list)
            pd.merge_pdf(pdf_files,'final.pdf')
            response = messagebox.showinfo("INFO","PDFs are merged to Mergerd_file.pdf in the same directory")
            Label(root,text=response).pack()
        except Exception as e:
            lg.error(e,"error occured at merging pdf ")



exe_button = Button(root,text='SUBMIT',padx=50,command=custom_command)
exe_button.grid(row=1,column=13)

clear_button = Button(root,text='Clear',padx=55,command=clear_func)
clear_button.grid(row=2,column=13)









root.mainloop()
lg.info("GUI has started")
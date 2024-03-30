# importing whole module
from tkinter import*
from tkinter.ttk import*
# importing strftimefunction to retrieve system time
from time import strftime
# creating tkinter window
root = Tk()
root.title('CLOCK')
# This function is used to display time on the label
def time():
    string = strftime('%H::%M::%S %p')
    Label.config(text = string)
    Label.after(1000,time)
    #Styling the label widget so that clock will look more attractive
    lbl = label(root, font = ('Calibri', 48,'bold'),
                background = 'black',
                foreground = 'white')
# placing clock at the centre of the tkinter window
Label.pack(root,anchor = 'center')
time()
mainloop()
import subprocess
from tkinter import *
from PIL import Image,ImageDraw
import opencv
import numpy




#Define Functions Here
def Open_File():
    #subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
    Image.open('C:\Test\happy.jpg').show()
def main_window(main):
    window.title('Facial Recognition')
    main.update_idletasks()
    width = 1024
    height = 768
    #find the center point of the width on the screen
    x = (main.winfo_screenwidth()//2)-(width//2)
    #find the center point of the height on the screen
    y = (main.winfo_screenheight()//2)-(height//2)

    main.geometry('{}x{}+{}+{}'.format(width,height,x,y))

    

#Define your Window
window = Tk()
main_window(window)

#Create Frames
topFrame = Frame(window)
topFrame.pack(side=LEFT)
bottomFrame = Frame(window)
bottomFrame.pack(side=RIGHT)

#Add Cascade Dropdown Menus
menu = Menu(window) #Add a Menu to the main window
window.config(menu=menu)

subMenu=Menu(menu)#declare a subMenu for menu
menu.add_cascade(label="File",menu=subMenu)#assign a dropdown for menu
subMenu.add_command(label="Open Image..",command =Open_File)
#Add a separator for your subMenu
subMenu.add_separator()
subMenu.add_command(label="Exit",command=exit)


#Add Buttons
##button1 = Button(topFrame,text="Open File...",fg="Grey",command=Open_File)
##button1.pack()
##button2 = Button(topFrame,text="Open Image...",fg="Dark Grey")
##button2.pack()


#Official Window loop continuously displays to screen
window.mainloop()


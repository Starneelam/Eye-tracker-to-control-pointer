from tkinter import *
import os

root=Tk()
root.title("Eye tracking system")
root.geometry("1315x680+135+90")
root.resizable(False,False)
# root.state('zoomed')  #zoomed

# root.overrideredirect(True) # it is for removing taskbar 

def Open():
    root.destroy()
    os.system("tracker.py")


root.configure(bg="#bcdeff")

#icon
image_icon=PhotoImage(file="icons/icon.png")
root.iconphoto(False,image_icon)

frame1=Frame(root,bg="#290e54",height=220)
frame1.pack(side=TOP,fill=X,padx=0,pady=0)

#logo
logo=PhotoImage(file="icons/logo1.png")

myimage1=Label(frame1,image=logo,background="#290e54")
myimage1.place(x=10,y=30)

Label(root,text="Eye Tracker",font="arial 30 bold",bg="#290e54",fg="white").place(x=399,y=60)

homepage_image=PhotoImage(file="images/homepage_image.png")
myimage3=Label(root,image=homepage_image,background="#bcdeff",bd=3)
myimage3.place(x=30,y=250)

homepage_image2=PhotoImage(file="images/Layer 6.png")
myimage4=Label(root,image=homepage_image2,background="#bcdeff")
myimage4.place(x=1100,y=240)

text_1=Label(root,text="I always take a close look at those who lose themselves in self portraits.",font="arial 12",bg="#bcdeff",fg="#6076a1")
text_1.place(x=720,y=400)

Start_button=PhotoImage(file="images/start_button.png")
myimage4=Button(root,image=Start_button,background="#bcdeff",activebackground="#bcdeff",bd=0,cursor='hand2',command=Open)
myimage4.place(x=700,y=470)

root.mainloop()





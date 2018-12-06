from tkinter import *
from tkinter import messagebox
import sys
root = Tk()

T1 = Label(root, text=' Select all images of birthday cake')
T1.config(font=("algerian", 13))
T1.place(height=40,width=350)


photo0 = PhotoImage(file="1st page\\reCaptcha.png")
l0 = Label(root, image=photo0)
l0.grid(row=0,column=4)

photo1 = PhotoImage(file="1st page\\cake1.png")
l1 = Label(root, image=photo1)
l1.grid(row=1,column=0)
CheckVar1 = IntVar()
C1 = Checkbutton(root, variable = CheckVar1, onvalue = 1, offvalue = 0, height=0,width = 0)
C1.grid(row=1,column=1)

photo2 = PhotoImage(file="1st page\\cake2.png")
l2 = Label(root, image=photo2)
l2.grid(row=2,column=0)
CheckVar2 = IntVar()
C2 = Checkbutton(root, variable = CheckVar2, onvalue = 1, offvalue = 0, height=0,width = 0)
C2.grid(row=2,column=1)

photo3 = PhotoImage(file="1st page\\cake3.png")
l3 = Label(root, image=photo3)
l3.grid(row=3,column=0)
CheckVar3 = IntVar()
C3 = Checkbutton(root, variable = CheckVar3, onvalue = 1, offvalue = 0, height=0,width = 0)
C3.grid(row=3,column=1)

photo4 = PhotoImage(file="1st page\\other1.png")
l4 = Label(root, image=photo4)
l4.grid(row=1,column=2)
CheckVar4 = IntVar()
C4 = Checkbutton(root, variable = CheckVar4, onvalue = 1, offvalue = 0, height=0,width = 0)
C4.grid(row=1,column=3)

photo5 = PhotoImage(file="1st page\\cake4.png")
l5 = Label(root, image=photo5)
l5.grid(row=2,column=2)
CheckVar5 = IntVar()
C5 = Checkbutton(root, variable = CheckVar5, onvalue = 1, offvalue = 0, height=0,width = 0)
C5.grid(row=2,column=3)

photo6 = PhotoImage(file="1st page\\other3.png")
l6 = Label(root, image=photo6)
l6.grid(row=3,column=2)
CheckVar6 = IntVar()
C6 = Checkbutton(root, variable = CheckVar6, onvalue = 1, offvalue = 0, height=-100,width = 0)
C6.grid(row=3,column=3)

photo7 = PhotoImage(file="1st page\\cake5.png")
l7 = Label(root, image=photo7)
l7.grid(row=1,column=4)
CheckVar7 = IntVar()
C7 = Checkbutton(root, variable = CheckVar7, onvalue = 1, offvalue = 0, height=0,width = 0)
C7.grid(row=1,column=5)

photo8 = PhotoImage(file="1st page\\other4 (1).png")
l8 = Label(root, image=photo8)
l8.grid(row=2,column=4)
CheckVar8 = IntVar()
C8 = Checkbutton(root, variable = CheckVar8, onvalue = 1, offvalue = 0, height=0,width = 0)
C8.grid(row=2,column=5)

photo9 = PhotoImage(file="1st page\\other2.png")
l9 = Label(root, image=photo9)
l9.grid(row=3,column=4)
CheckVar9 = IntVar()
C9 = Checkbutton(root, variable = CheckVar9, onvalue = 1, offvalue = 0, height=1,width = 0)
C9.grid(row=3,column=5)

def check():
    if (CheckVar9.get()==1 or CheckVar8.get()==1 or  CheckVar6.get()==1 or  CheckVar4.get()==1):
            refresh()
        
    else:
        messagebox.showinfo( "You are eligible", "You are not a robot")





def refresh():
    def check2():
         if (CheckVar8.get()==1 or CheckVar7.get()==1 or  CheckVar5.get()==1 or  CheckVar3.get()==1):
                                                        refresh2()
        
         else:
             messagebox.showinfo( "You are eligible", "You are not a robot")
    top = Toplevel()
    T1 = Label(top, text=' Select all images of dog')
    T1.config(font=("algerian", 16))
    T1.place(height=40,width=350)


    photo0 = PhotoImage(file="1st page\\reCaptcha.png")
    l0 = Label(top, image=photo0)
    l0.grid(row=0,column=4)

    photo1 = PhotoImage(file="2nd page\\dog1.png")
    l1 = Label(top, image=photo1)
    l1.grid(row=1,column=0)
    CheckVar1 = IntVar()
    C1 = Checkbutton(top, variable = CheckVar1, onvalue = 1, offvalue = 0, height=0,width = 0)
    C1.grid(row=1,column=1)

    photo2 = PhotoImage(file="2nd page\\dog4.png")
    l2 = Label(top, image=photo2)
    l2.grid(row=2,column=0)
    CheckVar2 = IntVar()
    C2 = Checkbutton(top, variable = CheckVar2, onvalue = 1, offvalue = 0, height=0,width = 0)
    C2.grid(row=2,column=1)

    photo3 = PhotoImage(file="2nd page\\animal2.png")
    l3 = Label(top, image=photo3)
    l3.grid(row=3,column=0)
    CheckVar3 = IntVar()
    C3 = Checkbutton(top, variable = CheckVar3, onvalue = 1, offvalue = 0, height=0,width = 0)
    C3.grid(row=3,column=1)

    photo4 = PhotoImage(file="2nd page\\dog2.png")
    l4 = Label(top, image=photo4)
    l4.grid(row=1,column=2)
    CheckVar4 = IntVar()
    C4 = Checkbutton(top, variable = CheckVar4, onvalue = 1, offvalue = 0, height=0,width = 0)
    C4.grid(row=1,column=3)

    photo5 = PhotoImage(file="2nd page\\animal4.png")
    l5 = Label(top, image=photo5)
    l5.grid(row=2,column=2)
    CheckVar5 = IntVar()
    C5 = Checkbutton(top, variable = CheckVar5, onvalue = 1, offvalue = 0, height=0,width = 0)
    C5.grid(row=2,column=3)

    photo6 = PhotoImage(file="2nd page\\dog3.png")
    l6 = Label(top, image=photo6)
    l6.grid(row=3,column=2)
    CheckVar6 = IntVar()
    C6 = Checkbutton(top, variable = CheckVar6, onvalue = 1, offvalue = 0, height=0,width = 0)
    C6.grid(row=3,column=3)

    photo7 = PhotoImage(file="2nd page\\animal1.png")
    l7 = Label(top, image=photo7)
    l7.grid(row=1,column=4)
    CheckVar7 = IntVar()
    C7 = Checkbutton(top, variable = CheckVar7, onvalue = 1, offvalue = 0, height=0,width = 0)
    C7.grid(row=1,column=5)

    photo8 = PhotoImage(file="2nd page\\animal5.png")
    l8 = Label(top, image=photo8)
    l8.grid(row=2,column=4)
    CheckVar8 = IntVar()
    C8 = Checkbutton(top, variable = CheckVar8, onvalue = 1, offvalue = 0, height=0,width = 0)
    C8.grid(row=2,column=5)

    photo9 = PhotoImage(file="2nd page\\dog5.png")
    l9 = Label(top, image=photo9)
    l9.grid(row=3,column=4)
    CheckVar9 = IntVar()
    C9 = Checkbutton(top, variable = CheckVar9, onvalue = 1, offvalue = 0, height=1,width = 0)
    C9.grid(row=3,column=5)

    B1 = Button(top, text = "Submit",bg="blue",fg="white",activebackground="orange",font="algerian",width=10,bd=5, command=check2)
    B1.grid(row=4,column=4)

   
        

   
   


    
    
    
    B2 = Button(top, text = "Refresh",bg="blue",fg="white",activebackground="orange",font="algerian",width=10,bd=5, command=refresh2)
    B2.grid(row=4,column=2)
    root.mainloop()

def refresh2():
    def check3():
        if (CheckVar1.get()==1 or CheckVar4.get()==1 or  CheckVar7.get()==1 or  CheckVar8.get()==1):
            messagebox.showinfo( "Warning", "You cross your limit")
            sys.exit()
                                                        
        
        else:
            messagebox.showinfo( "You are eligible", "You are not a robot")
    top = Toplevel()
    T1 = Label(top, text=' Select all images of storefront')
    T1.config(font=("algerian", 14))
    T1.place(height=40,width=350)


    photo0 = PhotoImage(file="1st page\\reCaptcha.png")
    l0 = Label(top, image=photo0)
    l0.grid(row=0,column=4)

    photo1 = PhotoImage(file="3rd page\\other4 .png")
    l1 = Label(top, image=photo1)
    l1.grid(row=1,column=0)
    CheckVar1 = IntVar()
    C1 = Checkbutton(top, variable = CheckVar1, onvalue = 1, offvalue = 0, height=0,width = 0)
    C1.grid(row=1,column=1)

    photo2 = PhotoImage(file="3rd page\\storefront5.png")
    l2 = Label(top, image=photo2)
    l2.grid(row=2,column=0)
    CheckVar2 = IntVar()
    C2 = Checkbutton(top, variable = CheckVar2, onvalue = 1, offvalue = 0, height=0,width = 0)
    C2.grid(row=2,column=1)

    photo3 = PhotoImage(file="3rd page\\storefront4.png")
    l3 = Label(top, image=photo3)
    l3.grid(row=3,column=0)
    CheckVar3 = IntVar()
    C3 = Checkbutton(top, variable = CheckVar3, onvalue = 1, offvalue = 0, height=0,width = 0)
    C3.grid(row=3,column=1)

    photo4 = PhotoImage(file="3rd page\\other1.png")
    l4 = Label(top, image=photo4)
    l4.grid(row=1,column=2)
    CheckVar4 = IntVar()
    C4 = Checkbutton(top, variable = CheckVar4, onvalue = 1, offvalue = 0, height=0,width = 0)
    C4.grid(row=1,column=3)

    photo5 = PhotoImage(file="3rd page\\storefront3.png")
    l5 = Label(top, image=photo5)
    l5.grid(row=2,column=2)
    CheckVar5 = IntVar()
    C5 = Checkbutton(top, variable = CheckVar5, onvalue = 1, offvalue = 0, height=0,width = 0)
    C5.grid(row=2,column=3)

    photo6 = PhotoImage(file="3rd page\\storefront2.png")
    l6 = Label(top, image=photo6)
    l6.grid(row=3,column=2)
    CheckVar6 = IntVar()
    C6 = Checkbutton(top, variable = CheckVar6, onvalue = 1, offvalue = 0, height=0,width = 0)
    C6.grid(row=3,column=3)

    photo7 = PhotoImage(file="3rd page\\other3.png")
    l7 = Label(top, image=photo7)
    l7.grid(row=1,column=4)
    CheckVar7 = IntVar()
    C7 = Checkbutton(top, variable = CheckVar7, onvalue = 1, offvalue = 0, height=0,width = 0)
    C7.grid(row=1,column=5)

    photo8 = PhotoImage(file="3rd page\\other2.png")
    l8 = Label(top, image=photo8)
    l8.grid(row=2,column=4)
    CheckVar8 = IntVar()
    C8 = Checkbutton(top, variable = CheckVar8, onvalue = 1, offvalue = 0, height=0,width = 0)
    C8.grid(row=2,column=5)

    photo9 = PhotoImage(file="3rd page\\storefront1.png")
    l9 = Label(top, image=photo9)
    l9.grid(row=3,column=4)
    CheckVar9 = IntVar()
    C9 = Checkbutton(top, variable = CheckVar9, onvalue = 1, offvalue = 0, height=1,width = 0)
    C9.grid(row=3,column=5)

    B1 = Button(top, text = "Submit",bg="blue",fg="white",activebackground="orange",font="algerian",width=10,bd=5, command=check3)
    B1.grid(row=4,column=4)

   
        

   
   
   


    root.mainloop()
        
B1 = Button(root, text = "Refresh",bg="blue",fg="white",activebackground="orange",font="algerian",width=10,bd=5,command = refresh)
B1.grid(row=4,column=2)

B2 = Button(root, text = "Submit",bg="blue",fg="white",activebackground="orange",font="algerian",width=10,bd=5,command=check)
B2.grid(row=4,column=4)



root.mainloop()    
   

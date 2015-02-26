from tkinter import *
from PIL import Image, ImageTk #to load images
from tkinter.constants import VERTICAL

'''
define a class that will hold gui and widgets
scrollable widgets are canvas, list,text - not Frame

we can use pack and grid in one application, but we can not use them in same frame.
example:
main frame is in grid (0,0)
canvas, frame.f1 and scrollbar are inside main frame and they are positioned with pack 
- you can not position one with pack and other with grid in same frame
labels in frame.f1 are positined with grid

this can not be achived with grid only - at least  do not know how...
'''
class myFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.my_data()
       

    def my_data(self):

        self.c1=Canvas(self)
        self.c1.config(bg="green",width=800,height=400) 
            
        self.s1=Scrollbar(self,orient=VERTICAL)
        self.s1.config(command=self.c1.yview)
        
        self.c1.config(yscrollcommand=self.s1.set)
        
        self.s1.pack(side="right", fill="y")
        self.c1.pack(side="left", fill="both", expand=True)
        
        self.f1=Frame(self.c1,bg="blue")
        self.f1.grid(row=1,column=10)
        self.f1.pack()
        self.f1.bind("<Configure>", self.OnFrameConfigure)
        
        self.c1.create_window((4,4), window=self.f1, anchor="nw",tags="self.f1")
        
        """1.jpg, 2.jpg, 3.jpg"""
        self.images=[]
        for i in range(1,4):
            self.img=Image.open(str(i)+".jpg")
            self.img1=ImageTk.PhotoImage(self.img)
            self.images.append(self.img1)
        
        """create label for each image"""
        self.l1=Label(self.f1,image=self.images[0])
        self.l1.grid(row=0,column=12)
        self.l1=Label(self.f1,image=self.images[1])
        self.l1.grid(row=1,column=12)
        self.l1=Label(self.f1,image=self.images[2])
        self.l1.grid(row=2,column=12)
        
        self.b1=Button(self,text="asdsaf")
        self.b1.pack(side="right")

        
        
    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        '''set ScrollRegion to size of inner frame'''
        self.c1.configure(scrollregion=self.c1.bbox("all"))    
        


def main():
    root=Tk()
    root.geometry("900x500")
    app=myFrame(root)
    app.config(bg="red")
    app.grid(row=0,column=0)
    app.mainloop()



main()     
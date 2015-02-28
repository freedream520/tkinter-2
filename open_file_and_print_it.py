from tkinter import *
from tkinter.filedialog import askopenfilename




class MyFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        
        self.parent=parent
        self.GUI()
        
        
        
    def OpenFile(self):
        self.fl=askopenfilename()
        try:
            self.f=open(self.fl)
            read_file=self.f.read()
            ''' delete content of text widget before you write new data'''
            self.t1.delete('1.0', END)
            for i in read_file:
                self.t1.insert(END,i)
            self.l1.config(text=self.fl)
        except:
            ''' if you click button to open file, and you close it, you will get
            error about non existing file... this can be better handled...'''
            self.l1.config(text="No File opened")
        
        
        
        
    def GUI(self):
        
        '''
        we create f1 so that button and label are inside that frame. this way 
        button (row=1) will not be as wide as text widget (also row=1)
        also, you neet to add sticky=ns to frame f1 in order to position button no top
        '''
        
        self.f1=Frame(self)
        self.f1.grid(row=1,column=1,sticky='ns')
        
        self.b1=Button(self.f1,text='Open File',command=self.OpenFile)
        self.b1.grid(row=1, column=1)
        
        
        self.l1=Label(self.f1,text='Waiting for File',width=20,wraplength=140)
        self.l1.grid(row=2,column=1)
        
        self.t1=Text(self,width=50,height=20)
        self.t1.insert('1.0', 'Waiting for text from file...')
        self.t1.grid(row=1,column=2)
        
        self.s1=Scrollbar(self,orient=VERTICAL)
        self.s1.config(command=self.t1.yview)
        self.s1.grid(row=1,column=3,sticky='ns')
        self.t1.config(yscrollcommand=self.s1.set)
        
       
       
def main():
    root=Tk()
    fr=MyFrame(root)
    fr.grid(row=0,column=0)
    
    root.mainloop()     
    
main() 
       
 
        





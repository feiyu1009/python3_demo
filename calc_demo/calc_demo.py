#encoding=utf-8
#简易计算器
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def showtext(self,event):
        self.entry1.insert(tk.END, event.widget.cget('text'))
        if event.widget.cget('text')=='=':
            input=self.entry1.get()
            self.entry1.delete(0,tk.END)
            res=eval(input[:-1])
            self.entry1.insert(tk.END,res)
        if event.widget.cget('text')=='C':
            self.entry1.delete(0,tk.END)
        
    def show_key_add(self,event):
        self.entry1.insert(tk.END,'+')

    def key_add_equas(self,event):
        if event.keycode==13:
            input=self.entry1.get()
            self.entry1.delete(0,tk.END)
            res=eval(input)
            self.entry1.insert(tk.END,res)
        if event.keycode==43:
            self.entry1.insert(tk.END,"+")
        if event.keycode==61:
            input=self.entry1.get()
            self.entry1.delete(0,tk.END)
            res=eval(input)
            self.entry1.insert(tk.END,res)


    def showcolor(self,event):
        event.widget['bg']='yellow'
        
    def recovercolor(self,event):
        event.widget['bg']='white'

    def showkey(self,event):
        self.entry1.insert(tk.END,event.char)

    def clear(self,event):
        self.entry1.delete(0,tk.END)

    def create_widgets(self):
        menubar=tk.Menu(self)   
        menubar.add_command(label='查看')
        menubar.add_command(label='编辑')
        menubar.add_command(label='帮助')
        root.config(menu=menubar)

        self.entry1=tk.Entry(self)
        self.entry1.grid(row=0,column=0,columnspan=5)
        blntext=(('MC','MR','MS','M+','C'),
        (7,8,9,'/','%'), (4,5,6,'*','1/x'), (1,2,3,'-','='),(0,'.','+'))
        for rowindex,r in enumerate(blntext):
            for cindex,c in enumerate(r):
                if c=='=':
                    self.btn1=tk.Button(self,width=2,text=c)
                    self.btn1.grid(row=rowindex+1,column=cindex,sticky='NSEW',rowspan=2,padx=1,pady=1)
                elif c==0:
                    tk.Button(self,width=2,text=c,name=c).grid(row=rowindex+1,column=cindex,sticky='EW',columnspan=2,padx=1,pady=1)
                elif c=='.' or c=='+':
                    tk.Button(self,width=2,text=c).grid(row=rowindex+1,column=cindex+1,sticky='EW',padx=1,pady=1)
            
                else:
                    tk.Button(self,width=2,text=c).grid(row=rowindex+1,column=cindex,sticky='EW',padx=1,pady=1)
        

        self.btn1.bind_class('Button','<Button-1>',self.showtext)
        self.btn1.bind_class('Button','<Enter>',self.showcolor)
        self.btn1.bind_class('Button','<Leave>',self.recovercolor)
        for i in range(9):
            root.bind('<KeyPress-{}>'.format(i),self.showkey)
        root.bind('<BackSpace>',self.clear)
        
        root.bind('<Key>',func=self.key_add_equas)
            
      
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('200x200')
    root.title('计算器')
    app = Application(master=root)   
    app.mainloop()


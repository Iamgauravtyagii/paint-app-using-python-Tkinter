from tkinter import *
import tkinter.font
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab


class PaintApp:

    def __init__(self,root):
        #setting up layout
        self.root = root
        self.root.title("PaintApp")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0,0)

        self.pen_color = "black"
        self.eraser_color = "white"

        #setting color window
        self.color_frame = LabelFrame(self.root,text='Color',font=('ariel',19,),bd=5,relief = RIDGE,bg="white")
        self.color_frame.place(x=0,y=0,width=70,height=185)


        #creating a color list
        colors = ['#FFFFCC','#00FFFF','#FFFF00','#FFFFFF','#000000','#00CC00','#FF66FF','#000033']
        i=j=0

        #iterating through the color list to save the colors in form of grid by using grid method
        for color in colors:
            Button(self.color_frame,bg=color,bd=2,relief=RIDGE,width=3,command= lambda col = color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1


        #now creating buttons
        self.eraser_button = Button(self.root,text="ERASER",bd=4,bg='white',command=self.eraser,width=6,relief=RIDGE)
        self.eraser_button.place(x=0,y=187)
        self.eraser_button = Button(self.root, text="CLEAR", bd=4, bg='white', command=lambda: self.canvas.delete("all"), width=6, relief=RIDGE)
        self.eraser_button.place(x=0, y=217)
        self.eraser_button = Button(self.root, text="SAVE", bd=4, bg='white', command=self.save_art,width=6, relief=RIDGE)
        self.eraser_button.place(x=0, y=247)
        self.eraser_button = Button(self.root, text="CANVAS", bd=4, bg='white', command=self.canavas_color, width=6, relief=RIDGE)
        self.eraser_button.place(x=0, y=277)

        #creating a scale bar

        self.size_scale_frame = LabelFrame(self.root,text='size',bd=5,bg='white',font=('ariel',15,'bold'),relief=RIDGE)
        self.size_scale_frame.place(x=0,y=310,height=200,width=70)

        self.size_scale = Scale(self.size_scale_frame,orient=VERTICAL,from_ =50,to=0,length=170)
        self.size_scale.set(1)
        self.size_scale.grid(row=0,column=1,padx=15)

        self.canvas = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=500,width=7000)
        self.canvas.place(x=80,y=0)

        #binding cursor with mouse drag
        self.canvas.bind("<B1-Motion>",self.paint)

    def paint(self,event):
        x1,y1 = (event.x-2),(event.y-2)
        x2,y2 = (event.x+2),(event.y+2)

        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.size_scale.get())

    def select_color(self,col):
        self.pen_color=col

    def eraser(self):
        self.pen_color= self.eraser_color

    def canavas_color(self):
        color = colorchooser.askcolor()
        print(color)
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

    def save_art(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            print(filename)
            x = self.root.winfo_rootx()+self.canvas.winfo_x()
            print(x, self.canvas.winfo_x())
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            print(y)
            x1 = x + self.canvas.winfo_width()
            print(x1)
            y1 = y + self.canvas.winfo_height()
            print(y1)
            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo('paint says','image is saved as'+str(filename))
        except:
            pass


if __name__ == "__main__":
    root = Tk()
    p = PaintApp(root)
    root.mainloop()

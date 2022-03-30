from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog

app = Tk()
app.title("image")
app.geometry("850x413")

app.iconbitmap("tuongclearlove7.png")

def Open():
    global My_img,My_Label,My_Label_Image,Filepath
    Filepath = filedialog.askopenfilename(
    initialdir="C:\\Users\\clearlove7\Documents\\GitHub\\clearlove7.github.io\\python",
    title="you are open file",
    filetypes=[
        ("MKV file", ".mkv"),
        ("PNG file", ".png"),
        ("All types", "*.*"),
        ("png files", "*png"),("jng files", "*jng"),
        ("Text Docs", "*.txt")
    ])
    My_Label = Label(app, text=Filepath).place(x=5,y=250)
    My_img = ImageTk.PhotoImage(Image.open(Filepath))
    My_Label_Image = Label(image=My_img).place(x=20,y=230)
my_button = Button(app, text="open file",command=Open).place(x=100,y=200)


app.mainloop()









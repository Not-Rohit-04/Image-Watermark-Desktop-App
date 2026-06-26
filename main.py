from tkinter import *
from tkinter import Tk, filedialog
from PIL import Image , ImageTk
from pathlib import Path

window = Tk()
window.minsize(400,400)
window.title("Mark-IT")

home_dir = Path.home()
def upload_img():
    file_path = filedialog.askopenfilename(
        parent=window,
        initialdir=home_dir,
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")],
    )


    if file_path:
        img = Image.open(file_path)
        img.thumbnail((100,100))
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img
        
        
title_label = Label(window,text='MARK--IT')
title_label.grid(row=0,column=0)

img_label = Label(window)
img_label.config(text='Select A image')
img_label.grid(row=1,column=1)       
        

upload_button = Button(window,text='Upload',command=upload_img)
upload_button.config(width=20)
upload_button.grid(row=2,column=1)
    


window.mainloop()

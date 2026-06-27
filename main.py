from tkinter import *
from tkinter import Tk, filedialog
from PIL import Image , ImageTk
from pathlib import Path


Win_bg = "#659287"
Img_label_bg ="#88BDA4"


window = Tk()
window.minsize(500,500)
window.config(padx=20,pady=20,bg=Win_bg)
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
        img_label.config(text="")
        img_label.config(width=0,height=0)
        img.thumbnail((400,400))
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img
        
        
canvas = Canvas(width=200,height=200,highlightthickness=0,bg=Win_bg)
icon_img = PhotoImage(file='assets/icon-img.png')
canvas.create_image(100,100,image=icon_img)
canvas.create_text(100,160,text='Mark-It',font=("Helvetica", 10, "bold"))
canvas.Image = icon_img
canvas.grid(row=0,column=1,columnspan=1,padx=20,pady=10)
        


container_frame = Frame(window,width=360,height=240,bg=Img_label_bg)
container_frame.grid(row=1, column=1, padx=20, pady=20)

container_frame.pack_propagate(False)
container_frame.grid_propagate(False)

img_label = Label(container_frame)
img_label.config(text='Clikc Upload to upload an image to add watermark',width=45,height=15,foreground='blue',bg=Img_label_bg,wraplength=300,justify='center')
img_label.pack(expand=True,fill='both')     
        

upload_button = Button(window,text='Upload',command=upload_img)
upload_button.config(width=20)
upload_button.grid(row=3,column=0,padx=20,pady=20)
    
    
add_watermark = Button(window,text='Add Watermark')
add_watermark.config(width=20)
add_watermark.grid(row=3,column=2,padx=20,pady=20)


watermark_label = Label(window,text='Enter Watermark')
watermark_label.config(background=Win_bg,width=20)
watermark_label.grid(row=2,column=1,padx=20,)

watermark_entry = Entry(window)
watermark_entry.focus_set()
watermark_entry.config(width=40)
watermark_entry.grid(row=3,column=1,padx=20)

window.mainloop()

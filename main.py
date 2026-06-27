from tkinter import *
from tkinter import filedialog , messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from pathlib import Path

Win_bg = "#659287"
Img_label_bg = "#88BDA4"


window = Tk()
window.minsize(500, 500)
window.config(padx=20, pady=20, bg=Win_bg)
window.title("Mark-IT")

home_dir = Path.home()

img = None
save_img = None

def image_save():
    global save_img
    save_path = filedialog.asksaveasfilename(
        parent=window,
        initialdir=home_dir,
        title="Save Watermarked Image",
        defaultextension=".png",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg;*.jpeg"),
            ("All Files", "*.*")
        ]
    )
    
    if save_path:
        try:
            save_img.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save image.\nError: {e}")

def watermark_addition():
    global img,save_img
    mark = watermark_entry.get()
    base_img = img.copy()
    draw = ImageDraw.Draw(base_img)
    font = ImageFont.truetype("arial.ttf", size=36)
    draw.text((50, 50), mark, fill=(255, 255, 255), font=font)
    preview_img = base_img.copy()
    preview_img.thumbnail((360, 240), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(preview_img)
    img_label.config(text="", image=tk_img)
    img_label.image = tk_img
    save_img = base_img
    save_button.config(state='normal')

def upload_img():
    file_path = filedialog.askopenfilename(
        parent=window,
        initialdir=home_dir,
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")],
    )

    if file_path:
        global img
        img = Image.open(file_path)
        preview = img.copy()
        img_label.config(text="")
        preview.thumbnail((360, 240), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(preview)
        img_label.config(image=tk_img)
        img_label.image = tk_img


canvas = Canvas(width=200, height=200, highlightthickness=0, bg=Win_bg)
icon_img = PhotoImage(file="assets/icon-img.png")
canvas.create_image(100, 100, image=icon_img)
canvas.create_text(100, 160, text="Mark-It", font=("Helvetica", 10, "bold"))
canvas.Image = icon_img
canvas.grid(row=0, column=1, columnspan=1, padx=20, pady=10)


container_frame = Frame(window, width=360, height=240, bg=Img_label_bg)
container_frame.grid(row=1, column=1, padx=20, pady=20)

container_frame.pack_propagate(False)
container_frame.grid_propagate(False)

img_label = Label(container_frame)
img_label.config(
    text="Clikc Upload to upload an image to add watermark",
    width=45,
    height=15,
    foreground="blue",
    bg=Img_label_bg,
    wraplength=300,
    justify="center",
)
img_label.pack(expand=True, fill="both")


upload_button = Button(window, text="Upload", command=upload_img)
upload_button.config(width=20)
upload_button.grid(row=3, column=0, padx=20, pady=20)


add_watermark_button = Button(window, text="Add Watermark", command=watermark_addition)
add_watermark_button.config(width=20)
add_watermark_button.grid(row=3, column=2, padx=20, pady=20)


watermark_label = Label(window, text="Enter Watermark")
watermark_label.config(background=Win_bg, width=20)
watermark_label.grid(
    row=2,
    column=1,
    padx=20,
)

watermark_entry = Entry(window)
watermark_entry.focus_set()
watermark_entry.config(width=40)
watermark_entry.grid(row=3, column=1, padx=20)

save_button = Button(window,text='Save',command=image_save)
save_button.config(width=30,state='disabled')
save_button.grid(row=4, column=1, padx=20, pady=20)

window.mainloop()

from tkinter import Tk, filedialog
from PIL import Image
from pathlib import Path

window = Tk()
window.config(height=400, width=400)
window.title("Mark-IT")

home_dir = Path.home()

file_path = filedialog.askopenfilename(
    parent=window,
    initialdir=home_dir,
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg")],
)


if file_path:
    img = Image.open(file_path)
    img.show()


window.mainloop()

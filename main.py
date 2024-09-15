# Import Modules
# tkinter Module for GUI Creation
from tkinter import *
# tkinter/filedialog Module for Browse files
from tkinter import filedialog
# Pillow Module for Open Images
from PIL import ImageTk, Image, ImageDraw, ImageFont

# Creation of Initial GUI
window = Tk()
window.title("Water-Mark Generator")
window.minsize(500, 500)
window.config(padx=20, pady=20)

# Function for Browsing Images
def imageBrowser():
    global new_img
    # Permit File Types in tkinter/filedialog
    fileTypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
    # Taking path with tkinter/filedialog
    path = filedialog.askopenfilename(filetypes=fileTypes)
    # Showing path in tkinter Entry Field
    path_entry.insert(END, string=path)
    # Opening new image with Pillow
    new_img = Image.open(path)
    initial_img = ImageTk.PhotoImage(new_img)
    # Showing new image in Canvas
    canvas.itemconfig(image_item, image=initial_img)

    # Keep a reference to the new image otherwise Image will not appear
    canvas.new_img = initial_img

# Adding Water-Mark
def waterMark():
    global op_image
    op_image = new_img.copy()
    img_size = op_image.size
    x = img_size[0] / 2
    y = img_size[1] / 2
    font = ImageFont.truetype("RobotoRegular-3m4L.ttf", 30)

    # Modifying the image
    draw = ImageDraw.Draw(op_image)
    # anchor="mm" place text in centre
    draw.text((x, y), mark_entry.get(), fill=(255, 255, 255, 128), font=font, anchor="mm")

    watermarked_img = ImageTk.PhotoImage(op_image)
    # Showing new image in Canvas
    canvas.itemconfig(image_item, image=watermarked_img)

    # Keep a reference to the new image otherwise Image will not appear
    canvas.new_img = watermarked_img

# Destination Browsing
def saveImage():
    file_types = [("Image Files", "*.png;*.jpg;*.jpeg")]
    dest_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".png")
    final_image = op_image
    final_image.save(dest_path)

# Creation of title label
first_label = Label(text="Welcome to Water-Mark Generator", font=("courier", 12, "bold"))
first_label.grid(row=0, column=1)

# Creation of Water Mark Label and Entry
mark_label = Label(text="Water-Mark Text:", font=("courier", 8, "normal"))
mark_label.grid(row=1, column=0)

mark_entry = Entry(width=50)
mark_entry.focus()
mark_entry.grid(row=1, column=1)

# Creation of Browse Button
browse_button = Button(text="Browse", command=imageBrowser)
browse_button.grid(row=2, column=0)

# Creation of Entry for Path
path_entry = Entry(width=50)
path_entry.focus()
path_entry.grid(row=2, column=1)

# Creation of Upload Button
mark_button = Button(text="Add Water-Mark", command=waterMark)
mark_button.grid(row=2, column=2)

# Creation of Canvas
canvas = Canvas(width=480, height=480)
# Opening Image with Pillow
image = Image.open("default.png")
default_img = ImageTk.PhotoImage(image)
# Showing Image in Canvas
image_item = canvas.create_image(240, 240, image=default_img)
canvas.grid(row=3, columnspan=3)

# Destination
# Save Button
save_button = Button(text="Save Image", command=saveImage)
save_button.grid(row=4, column=1)

window.mainloop()
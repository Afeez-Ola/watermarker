import numpy as np
from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
import cv2


def watermarkAdder():
    file1 = browseFile()
    file2 = browseFile()
    logo = Image.open(file2).convert("RGBA")
    product = cv2.imread(file1)

    product_size = product.shape[:2]
    logo = logo.resize((int(product_size[1] * 0.2), int(product_size[0] * 0.2)))

    logo_width, logo_height = logo.size
    position = (product_size[1] - logo_width, product_size[0] - logo_height)

    logo_cv = np.array(logo)
    alpha_channel = logo_cv[:, :, 3]

    # Create a mask for the alpha channel
    alpha_mask = alpha_channel / 255.0
    product_copy = product.copy()
    for c in range(0, 3):
        product[position[1]:position[1] + logo_height, position[0]:position[0] + logo_width, c] = \
            (1 - alpha_mask) * product[position[1]:position[1] + logo_height,position[0]:position[0] + logo_width, c] + \
            alpha_mask * logo_cv[:, :, c]

    cv2.imwrite('watermarked_image.jpg', product)
    print("Watermark successfully added!")


def browseFile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Image files",
                                                      ["*.jpg*", "*.png*", "*.webp*"]),
                                                     ("all files",
                                                      "*.*")))
    return filename


app = tk.Tk()
app.title("Watermark Adder")

# Create a label for the watermark text
watermark_label = tk.Label(app, text="Watermark Text:")
watermark_label.pack()

# Create an entry field for the watermark text
watermark_entry = tk.Entry(app)
watermark_entry.pack()

label_file_explorer = tk.Label(app,
                               text="File Explorer using Tkinter \nSelect your image first and then select the logo. \nYou can do this by clicking on 'Add Watermark' button!",
                               width=100, height=4, fg="blue")
label_file_explorer.pack()
# Create a button to add the watermark
add_button = tk.Button(app, text="Add Watermark", command=watermarkAdder)
add_button.pack()

# Run the application
app.mainloop()

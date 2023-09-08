import numpy as np
from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
import cv2


def watermarkAdder():
    image_file = browseFile("Select an image",
                            [("Image files", ["*.jpg", "*.png", "*.webp"]), ("All files", "*.*")])
    logo_file = browseFile("Select a logo", [("Image files", ["*.png"]), ("All files", "*.*")])

    if not image_file or not logo_file:
        return

    watermark = Image.open(logo_file).convert("RGBA")
    product = cv2.imread(image_file)

    product_size = product.shape[:2]
    watermark = watermark.resize((int(product_size[1] * 0.2), int(product_size[0] * 0.2)))

    watermark_width, watermark_height = watermark.size
    position = (product_size[1] - watermark_width, product_size[0] - watermark_height)

    watermark_cv = np.array(watermark)
    alpha_channel = watermark_cv[:, :, 3]

    alpha_mask = alpha_channel / 255.0
    product_copy = product.copy()

    for c in range(0, 3):
        product[position[1]:position[1] + watermark_height, position[0]:position[0] + watermark_width, c] = \
            (1 - alpha_mask) * product[position[1]:position[1] + watermark_height,
                               position[0]:position[0] + watermark_width, c] + \
            alpha_mask * watermark_cv[:, :, c]

    output_file = 'watermarked_image.jpg'
    cv2.imwrite(output_file, product)
    print(f"Watermark successfully added to {output_file}")


def browseFile(title,filetype):
    filename = filedialog.askopenfilename(initialdir="/",
                                          title=title,
                                          filetypes=filetype)
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

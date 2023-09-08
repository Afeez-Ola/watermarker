Watermark Adder
===============

The Watermark Adder is a Python application that allows you to add a watermark logo to an image. It's built using Python's tkinter for the graphical user interface (GUI), OpenCV for image processing, and the Python Imaging Library (PIL) for handling images.

Features
--------

-   Select an image file (e.g., JPG, PNG, WEBP).
-   Select a logo file (must be in PNG format for transparency).
-   Automatically resizes the logo to fit 20% of the image size.
-   Adds the logo as a watermark to the bottom-right corner of the image.
-   Maintains transparency of the watermark logo.

Getting Started
---------------

To use the Watermark Adder:

1.  Clone or download this repository to your local machine.

2.  Ensure you have the required libraries installed:

    -   `numpy`
    -   `PIL` (Pillow)
    -   `tkinter`
    -   `cv2` (OpenCV)

    You can install these libraries using pip:

    bashCopy code

    `pip install numpy pillow tk opencv-python-headless`

3.  Run the `watermark_adder.py` script:

    bashCopy code

    `python watermark_adder.py`

4.  The application will open, allowing you to select an image and a logo to add as a watermark.

5.  Click the "Add Watermark" button, and the watermarked image will be saved as `watermarked_image.jpg` in the same directory.


License
-------

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.

Acknowledgments
---------------

-   Thanks to the Python community for the libraries used in this project.
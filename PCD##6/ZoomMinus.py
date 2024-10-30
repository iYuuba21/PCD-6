import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoom(image, factor):
    """
    Zooms in (factor > 1) or out (factor < 1) on an image.

    Args:
        image: The original image as a NumPy array.
        factor: The zoom factor. A value greater than 1 zooms in, 
              a value less than 1 zooms out.

    Returns:
        The zoomed image as a NumPy array.
    """

    height, width = image.shape[:2]

    # Handle negative factors for zooming out
    if factor < 1:
        new_factor = 1.0 / factor  # Invert factor for zoom out
    else:
        new_factor = factor

    # Calculate new dimensions considering potential rounding errors
    new_height = int(height * new_factor + 0.5)
    new_width = int(width * new_factor + 0.5)

    # Create a new empty image with the same data type as the original
    img_zoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    # Loop through each pixel in the zoomed image
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the corresponding coordinates in the original image
            orig_y = int(y / new_factor)
            orig_x = int(x / new_factor)

            # Ensure coordinates are within the original image bounds
            orig_y = min(orig_y, height - 1)
            orig_x = min(orig_x, width - 1)

            # Assign the pixel value from the original image to the new image
            img_zoom[y, x] = image[orig_y, orig_x]

    return img_zoom

# Load the image
image = img.imread("C:/Users/Ev/Pictures/wanda.jpeg")

# Zoom out by a factor of 0.5 (can be adjusted for different zoom levels)
zoom_factor = 0.5
zoomed_image = zoom(image, zoom_factor)

# Save the zoomed image (optional)
# img.imwrite("D:\\z_out.jpg", zoomed_image)

# Display the original and zoomed images
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 2, 2)
plt.imshow(zoomed_image)
plt.title("Gambar Setelah Diperkecil")

plt.show()
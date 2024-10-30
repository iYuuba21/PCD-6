import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

# Path ke gambar
path = "C:/Users/Ev/Pictures/wanda.jpeg"
image = img.imread(path)

# Mendapatkan tinggi dan lebar gambar
height, width = image.shape[:2]

# Membuat array kosong dengan ukuran yang sama dengan gambar asli
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)

# Membalik gambar secara horizontal (kiri-kanan)
for y in range(height):
    for x in range(width):
        horizontal[y, x] = image[y, width - 1 - x]

# Membalik gambar secara vertikal (atas-bawah)
for y in range(height):
    for x in range(width):
        vertical[y, x] = image[height - 1 - y, x]

# Menampilkan gambar asli, horizontal flip, dan vertical flip
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 3, 2)
plt.imshow(horizontal)
plt.title("Horizontal Flip")

plt.subplot(1, 3, 3)
plt.imshow(vertical)
plt.title("Vertical Flip")

plt.show()

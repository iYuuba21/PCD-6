import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

# Path ke gambar
path = "C:/Users/Ev/Pictures/wanda.jpeg"
image = img.imread(path)

# Mendapatkan tinggi dan lebar gambar
height, width = image.shape[:2]

# Membuat array kosong untuk gambar yang akan di-mirror
mirrored = np.zeros_like(image)

# Membalik gambar secara horizontal dan vertikal
for y in range(height):
    for x in range(width):
        mirrored[y, x] = image[height - 1 - y, width - 1 - x]

# Menampilkan gambar asli dan gambar yang di-mirror
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 2, 2)
plt.imshow(mirrored)
plt.title("Gambar Mirror")

plt.show()
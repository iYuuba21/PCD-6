import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree, pivot=(0, 0)):
    # Konversi derajat ke radian
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    # Mendapatkan tinggi dan lebar gambar
    height, width = image.shape[:2]

    # Hitung dimensi maksimum yang dibutuhkan untuk gambar setelah rotasi
    max_dim = int(np.sqrt(height**2 + width**2))
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)

    # Titik pusat rotasi (sudah diberikan sebagai parameter)
    centerX, centerY = pivot

    # Proses rotasi dengan memetakan setiap piksel
    for y in range(height):
        for x in range(width):
            # Hitung koordinat baru setelah rotasi relatif terhadap titik pusat
            newX = int(cos_deg * (x - centerX) - sin_deg * (y - centerY)) + centerX
            newY = int(sin_deg * (x - centerX) + cos_deg * (y - centerY)) + centerY

            # Memastikan koordinat baru berada dalam batas dimensi output
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y, x]

    return outputImage

# Membaca gambar dari path
image = img.imread("C:/Users/Ev/Pictures/wanda.jpeg")

# Rotasi gambar sebesar 45 derajat dengan titik pusat di (0,0)
rotated_image = rotateImage(image, 45, pivot=(0, 0))

# Menampilkan gambar asli dan gambar hasil rotasi
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Gambar Setelah Rotasi")

plt.show()
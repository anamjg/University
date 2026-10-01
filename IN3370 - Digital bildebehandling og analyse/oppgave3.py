from PIL import Image
from scipy import signal, fft
import numpy as np 
import matplotlib.pyplot as plt 

""" Upload of image cow.png"""
filename = "c:\\Users\\anita\\OneDrive\\Documents\\Høst2024\\IN3770\\oblig2\\cow.png"
image = Image.open(filename).convert('L') # 'L' mode ensures the image is grayscale
image = np.array(image)

# lavpassfilter ved hjelp av sirkelutformet, velg radius slik at likner 15x15 convolve2d
n, m = image.shape 
D0 = 0.09
H = np.zeros((n, m))

for u in range(n):
    for v in range(m):
        D = np.sqrt(((u-0.5*n)/(0.5*n))**2+((v-m*0.5)/(m*0.5))**2)
        if D <= D0:
            H[u,v] = 1
            
F = fft.fft2(image)
img_h = (fft.ifft2(F*fft.fftshift(H))).real

kernel = np.ones((15,15)) / 225 

# Filter with boundary='fill'
img_fill = signal.convolve2d(image, kernel, boundary='wrap')

plt.figure()
plt.subplot(1, 2, 1)
plt.title("Boundary = 'wrap'")
plt.imshow(img_fill, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title(f"Ideelt lavpassfilter med D0 = {D0}")
plt.imshow(img_h, cmap='gray')
plt.axis('off')
plt.show()

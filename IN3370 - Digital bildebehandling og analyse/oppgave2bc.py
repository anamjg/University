from PIL import Image
from scipy import signal, fft
import time 
import numpy as np 
import matplotlib.pyplot as plt 

""" Upload of image cow.png"""
filename = "c:\\Users\\anita\\OneDrive\\Documents\\Høst2024\\IN3770\\oblig2\\cow.png"
image = Image.open(filename).convert('L') # 'L' mode ensures the image is grayscale
image = np.array(image)

def fft_fill(image, kernel):
    pad_shape = (image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1)

    image_padded = np.pad(image, ((0, pad_shape[0] - image.shape[0]), (0, pad_shape[1] - image.shape[1]))) 
    kernel_padded = np.pad(kernel, ((0, pad_shape[0] - kernel.shape[0]), (0, pad_shape[1] - kernel.shape[1]))) 

    # Perfom FFT on both padded image and kernel 
    image_fft = fft.fft2(image_padded)
    kernel_fft = fft.fft2(kernel_padded)

    # Multiply in the frequency domain and do the inverse FFT 
    fill_fft = fft.ifft2(image_fft * kernel_fft).real
    
    return fill_fft


def fft_wrap(image, kernel):
    # 'wrap' with FFT 
    padded_kernel = np.zeros(image.shape)
    padded_kernel[:kernel.shape[0], :kernel.shape[1]] = kernel 

    # Perfom FFT on both padded image and kernel
    fft_image = fft.fft2(image)
    fft_kernel = fft.fft2(padded_kernel)

    # Multiply in the frequency domain and do the inverse FFT 
    wrap_fft = fft.ifft2(fft_image * fft_kernel).real
    
    return wrap_fft

# Gjennomsnittlig kjøretid og standaravvik 
kernel_size = [3, 5, 7, 15, 31, 63]

# Data for fill 
means_convolve2d_fill = []
std_devs_convolve2d_fill = []
means_fft_fill = []
std_devs_fft_fill = []

# Data for wrap 
means_convolve2d_wrap = []
std_devs_convolve2d_wrap = []
means_fft_wrap = []
std_devs_fft_wrap = []

for size in kernel_size:
    print(f"Kernel size is {size}x{size}")
    kernel = np.ones((size, size)) / size**2
    times_convolve2d_fill = []
    times_fft_fill = []
    times_convolve2d_wrap = []
    times_fft_wrap = []
    i = 0
    while i<25: 
        # Time for convolve2d 'fill'
        start_time = time.time()
        img_fill = signal.convolve2d(image, kernel, boundary='fill')
        end_time = time.time()
        time_convolve2d_fill = end_time - start_time 
        times_convolve2d_fill.append(time_convolve2d_fill)
        
        # Time for FFT 'fill'
        start_time = time.time()
        fill_fft = fft_fill(image, kernel)    
        end_time = time.time()
        time_fft_fill = end_time - start_time
        times_fft_fill.append(time_fft_fill)
        
        # Time for convolve2d 'wrap'
        start_time = time.time()
        img_wrap = signal.convolve2d(image, kernel, boundary='wrap')
        end_time = time.time()
        time_convolve2d_wrap = end_time - start_time
        times_convolve2d_wrap.append(time_convolve2d_wrap)
        
        # Time for FFT 'wrap'
        start_time = time.time()
        wrap_fft = fft_wrap(image, kernel)    
        end_time = time.time()
        time_fft_wrap = end_time - start_time
        times_fft_wrap.append(time_fft_wrap)
        
        i += 1
        
    means_convolve2d_fill.append(np.mean(times_convolve2d_fill))
    std_devs_convolve2d_fill.append(np.std(times_convolve2d_fill))
    means_fft_fill.append(np.mean(times_fft_fill))
    std_devs_fft_fill.append(np.std(times_fft_fill))
    
    
    means_convolve2d_wrap.append(np.mean(times_convolve2d_wrap))
    std_devs_convolve2d_wrap.append(np.std(times_convolve2d_wrap))
    means_fft_wrap.append(np.mean(times_fft_wrap))
    std_devs_fft_wrap.append(np.std(times_fft_wrap))

print("Trying to plot now")
plt.figure(figsize=(10,5))
plt.errorbar(kernel_size, means_convolve2d_fill, yerr=std_devs_convolve2d_fill, fmt='o-', capsize=5,
             label='Convolve2d fill', color='orange')
plt.errorbar(kernel_size, means_fft_fill, yerr=std_devs_fft_fill, fmt='o-', capsize=5,
             label='FFT fill', color='red')
plt.errorbar(kernel_size, means_convolve2d_wrap, yerr=std_devs_convolve2d_wrap, fmt='o-', capsize=5,
             label='Convolve2d wrap', color='green')
plt.errorbar(kernel_size, means_fft_wrap, yerr=std_devs_fft_wrap, fmt='o-', capsize=5,
             label='FFT wrap', color='blue')
plt.xlabel('Kernel Size (NxN)')
plt.ylabel('Mean Execution Time (seconds)')
plt.title('Mean Execution Time of convolve2d and fft with Standard Deviation')
plt.xticks(kernel_size)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


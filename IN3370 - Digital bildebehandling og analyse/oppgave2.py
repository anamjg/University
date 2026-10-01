import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
filename = 'c:\\Users\\anita\\OneDrive\\Documents\\Høst2024\\IN3770\\oblig1\\cellekjerner.png'
img = Image.open(filename).convert('L') # 'L' mode ensures the image is grayscale
image = np.array(img)
    
def convolve(image, kernel):
    """Apply convolution of an image with a given kernel."""
    img_height, img_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # Padding the image to handle borders
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='edge')

    # Initialize the output
    output = np.zeros_like(image)

    # Apply convolution
    for i in range(img_height):
        for j in range(img_width):
            # Element-wise multiplication and summing the result
            neighborhood = padded_image[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(kernel * neighborhood)
    return output

def gaussian_kernel(size, sigma):
    """Generates a Gaussian kernel."""
    kernel = np.zeros((size, size))
    center = size // 2
    total_sum = 0  # Normalization constant

    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            value = (1/(2*np.pi*sigma**2)) * np.exp(-(x**2 + y**2) / (2*sigma**2))
            kernel[i, j] = value
            total_sum += value

    # Normalize the kernel so the sum of all elements is 1
    kernel = kernel / total_sum
    return kernel

def sobel_filters(image):
    """Apply Sobel filters to estimate gradients."""
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # Sobel X
    Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # Sobel Y

    Ix = convolve(image, Kx)
    Iy = convolve(image, Ky)

    G = np.hypot(Ix, Iy)  # Magnitude of the gradient
    theta = np.arctan2(Iy, Ix)  # Direction of the gradient
    return G, theta

def non_max_suppression(G, theta):
    """Thin edges by suppressing non-maximum gradient magnitudes."""
    M, N = G.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = theta * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M-1):
        for j in range(1, N-1):
            try:
                q = 255
                r = 255

                # Angle 0 (horizontal neighbors)
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = G[i, j+1]
                    r = G[i, j-1]
                # Angle 45 (diagonal neighbors - top-right and bottom-left)
                elif 22.5 <= angle[i, j] < 67.5:
                    q = G[i+1, j-1]
                    r = G[i-1, j+1]
                # Angle 90 (vertical neighbors)
                elif 67.5 <= angle[i, j] < 112.5:
                    q = G[i+1, j]
                    r = G[i-1, j]
                # Angle 135 (diagonal neighbors - top-left and bottom-right)
                elif 112.5 <= angle[i, j] < 157.5:
                    q = G[i-1, j-1]
                    r = G[i+1, j+1]

                if (q == 0 or r == 0):
                    Z[i, j] = G[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    return Z

# Thresholding Based on Intensity
def intensity_threshold(image, threshold=100):
    """Keeps only pixels darker than the threshold (darker elements)."""
    return np.where(image < threshold, image, 0)

# Canny Edge Detection Implementation
def canny_edge_detection(image, sigma=1, low_threshold=0.1, high_threshold=0.3, intensity_thresh=100):
    """Complete Canny Edge Detection algorithm to focus on darker elements."""
    # Step 1: Gaussian filter
    size = int(2*(np.ceil(3*sigma))+1)
    smoothed_image = convolve(image, gaussian_kernel(size, sigma))

    # Step 2: Apply intensity thresholding to isolate darker elements
    dark_elements = intensity_threshold(smoothed_image, intensity_thresh)
      
    # Step 3: Get gradient magnitudes and angles
    G, theta = sobel_filters(dark_elements)

    # Step 4: Non-maximum suppression
    non_max_img = non_max_suppression(G, theta)

    # Step 5: Double threshold
    strong = non_max_img > high_threshold
    weak = (non_max_img > low_threshold) & (non_max_img <= high_threshold)

    output = np.zeros(non_max_img.shape)
    output[strong] = 255
    output[weak] = 75

    return output

# Apply the Canny Edge Detection focusing on darker elements
edges = canny_edge_detection(image, sigma=2, low_threshold=0.1, high_threshold=0.3, intensity_thresh=120)

plt.figure()
plt.title("Cellekjerne med sigma=2, T_l = 0.1, T_h=0.3")
plt.imshow(edges, cmap='gray', vmin=0, vmax=255)
plt.axis("off")
plt.show()
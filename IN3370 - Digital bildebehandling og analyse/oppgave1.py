
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
#  DEL 1 
# Standardisere kontrasten slik at 
# - middelverdi er på rundt 127
# - standardavvik på rundt 64
 
filename = 'c:\\Users\\anita\\OneDrive\\Documents\\Høst2024\\IN3770\\oblig1\\portrett.png'
img = Image.open(filename).convert('L') # 'L' mode ensures the image is grayscale
img = np.array(img)
n, m = img.shape

# Regner middelverdien 
def mid_verdi_regning(n, m, img):
    temp = 0
    for i in range(0, n-1):
        for j in range(0, m-1):
            temp += img[i,j]/(n*m)
    return temp

mid_verdi = mid_verdi_regning(n,m,img) 

# Regner varians og standardavvik 
def varians_regning(n,m,img, mid_verdi):
    temp = 0
    for i in range(0, n-1):
        for j in range(0, m-1):
            temp += (img[i,j] - mid_verdi)**2
    return temp/(n*m)
 
varians = varians_regning(n,m,img, mid_verdi)
standard = np.sqrt(varians)

#  Calculate the new a and b
a = 64/standard
b = 127 - a*mid_verdi

new_img = img*a +b 

plt.figure()
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Endring av kontrast")
plt.imshow(new_img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# DEL 2 
# Standardisere geometrien 
# Slik at øyne og munn passer over masken 

filename = 'C:\\Users\\anita\\OneDrive\\Documents\\Høst2024\\IN3770\\oblig1\\geometrimaske.png'
mask = Image.open(filename).convert('L') # 'L' mode ensures the image is grayscale
geometrimaske = np.array(mask)
N, M = geometrimaske.shape

# Now we use this equations to find the constants 
a_0 = 3.022
a_1 = -3.211
a_2 = 201.956
b_0 = 2.309
b_1 = 4.041
b_2 = -295.618
C = np.array([[a_0, a_1, a_2],
              [b_0, b_1, b_2],
              [0,    0,    1]])

def affin_trans(n, m, img, C, N, M):
    output_image = np.zeros((N,M))
    
    for i in range(n):
        for j in range(m):
            new_pixel = C @ np.array([j, i, 1])
            new_pixel = new_pixel.astype(int)
            if 0 <= new_pixel[0] < M and 0 <= new_pixel[1] < N:
                output_image[new_pixel[1], new_pixel[0]] = img[i,j]
                
    return output_image

trans_img = affin_trans(n, m, new_img, C, N, M)

plt.figure()
plt.title("Portrett etter forlengstransformajson")
plt.imshow(trans_img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

inv_C = np.linalg.inv(C)

#Function to compute the neighbor interpolation 
def nearest_neighbor_interpolation(n, m, img, inv_C, N, M):
    output_image = np.zeros((N, M))

    for i in range(N):
        for j in range(M):
            transformed_coords = inv_C @ np.array([j, i, 1])
            x_new = round(transformed_coords[0])
            y_new = round(transformed_coords[1])
            if 0 <= x_new < m and 0 <= y_new < n:
                output_image[i,j] = img[y_new, x_new]
    
    return output_image

neigh_trans= nearest_neighbor_interpolation(n, m, new_img, inv_C, N, M)

plt.figure()
plt.title("Portrett etter nabointerpolasjon")
plt.imshow(neigh_trans, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

#Function to compute the bilinear interpolation 
def bilinear_interpolation(img, inv_C, N, M):
    output_image = np.zeros((N, M))
    n, m = img.shape

    for i in range(N):
        for j in range(M):
            transformed_coords = inv_C @ np.array([j, i, 1])
            x = transformed_coords[0]
            y = transformed_coords[1]
            
            # Ensure coordinates are within bounds
            if x < 0 or x >= m - 1 or y < 0 or y >= n - 1:
                continue  # Skip interpolation for out of bounds points
            
            
            # Finding the four neighbors 
            x_1 = int(np.floor(x))
            y_1 = int(np.floor(y))
            x_2 = min(x_1 + 1, m - 1)
            y_2 = min(y_1 + 1, n - 1)
            
            # Get the pixel values
            Q_11 = img[y_1, x_1]
            Q_21 = img[y_1, x_2]
            Q_12 = img[y_2, x_1]
            Q_22 = img[y_2, x_2]
            
            # Handle possible division by zero (if x_1 == x_2 or y_1 == y_2)
            if x_2 == x_1:
                x_weight = 0
            else:
                x_weight = (x - x_1) / (x_2 - x_1)
            
            if y_2 == y_1:
                y_weight = 0
            else:
                y_weight = (y - y_1) / (y_2 - y_1)

            # Bilinear interpolation formula
            top = (1 - x_weight) * Q_11 + x_weight * Q_21
            bottom = (1 - x_weight) * Q_12 + x_weight * Q_22
            output_image[i, j] = (1 - y_weight) * top + y_weight * bottom
               
    return output_image

bilin_trans = bilinear_interpolation(new_img, inv_C, N, M)


plt.figure()
plt.title("Portrett etter bilineær interpolasjon")
plt.imshow(bilin_trans, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()
from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt
import cv2


# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


# read lena RGB image and convert to grayscale
im = imread('Lenna.png')
im_R = im[:, :, 0]
im_G = im[:, :, 1]
im_B = im[:, :, 2]

im_dct_R = dct2(im_R)
im_dct_G = dct2(im_G)
im_dct_B = dct2(im_B)

im_idct_R = idct2(im_dct_R)
im_idct_G = idct2(im_dct_G)
im_idct_B = idct2(im_dct_B)

im1 = cv2.merge((im_idct_R, im_idct_G, im_idct_B)).astype(int)


# check if the reconstructed image is nearly equal to the original image
np.allclose(im, im1)
# True

# plot original and reconstructed images with matplotlib.pylab
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original image',
                                                             size=20)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title(
    'reconstructed image (DCT+IDCT)', size=20),

plt.savefig('plot.png')

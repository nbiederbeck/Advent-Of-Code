import numpy as np

def reconstruct(l, x=25, y=6):
    layers = int(len(l) / x / y)
    img = np.asarray([i for i in l], dtype='int')
    img = img.reshape((layers, y * x))
    return img

def fewest_zeros(im):
    n_zeros = np.sum(im == 0, axis=1)
    idx = np.argmax(n_zeros)
    return idx

def multiply_ones_twos(im, idx):
    n_ones = np.sum(im[idx, :] == 1)
    n_twos = np.sum(im[idx, :] == 2)

    return n_ones * n_twos

def space_image(riddle, x, y):
    img = reconstruct(riddle[0], x, y)
    idx = fewest_zeros(img)
    ans = multiply_ones_twos(img, idx)
    return ans

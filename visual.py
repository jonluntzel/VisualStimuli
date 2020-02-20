"""
Top-Level Description
"""
#methods are modified to work with arrays that have no third rgb index. could add the option to use rgb images as well later.
import numpy as np
import random
from skimage.transform import resize
from skimage.transform import rotate

#remove thiss guy later
import matplotlib.pyplot as plt

imgwlarge = np.load("imgwlarge.npy")

#compress by a factor of x, any positive finite real number
def compressx(img, factor):
    sub1 = int(np.rint((img.shape[0] - (img.shape[0] / factor)) / 2))
    sub2 = int(np.rint((img.shape[1] - (img.shape[1] / factor)) / 2))
   
    im2 = imgwlarge.copy() #[:,:,0]
#    im2 = imgw.copy() #(use this line if input is 800x800)
    
    shrunk = resize(img.copy(), (int(img.shape[0] / factor), int(img.shape[1] / factor), int(img.shape[2]))) * 255 #* 255
    
#     im2[100+sub1:100+(shrunk.shape[0]+sub1),200+sub2:200+(shrunk.shape[1]+sub2)] = shrunk
    im2[sub1:(shrunk.shape[0]+sub1),sub2:(shrunk.shape[1]+sub2),:] = shrunk
    print(sub1, sub2, shrunk.shape, im2.shape)
#     print("compressx")
#     plt.figure()
#     plt.imshow(im2)
    return im2

# def compressx(img, factor):
#     sub1 = int((img.shape[0] - (img.shape[0] / factor)) / 2)
#     sub2 = int((img.shape[1] - (img.shape[1] / factor)) / 2)
    
#     im2 = imgwlarge.copy() #[:,:,0]
# #    im2 = imgw.copy() #(use this line if input is 800x800)
    
#     shrunk = resize(img.copy(), (int(img.shape[0] / factor), int(img.shape[1] / factor), int(img.shape[2]))) * 255 #* 255
    
# #     im2[100+sub1:100+(shrunk.shape[0]+sub1),200+sub2:200+(shrunk.shape[1]+sub2)] = shrunk
#     im2[sub1:(shrunk.shape[0]+sub1),sub2:(shrunk.shape[1]+sub2),:] = shrunk
    
#     return im2

#introduces noise into images. imgs is an array of flattened images, and r is the fraction of pixels flipped
def groupswitch(imgs, r, d):
    copy = imgs #use this to see images.reshape(size, 800, 800,3)
    #copy = imgs.copy() if you don't want to modify the original
    w, h = d, d
    for i in copy:
        for j in range(0, d*d):
            c = random.random()
            if (c <= r):
                if (i[j] == 1.0) or (i[j] == 255):
                    i[j] = 0
                else:
                    i[j] = 255
    return copy

#         for j in range(0, 800*800*3, 3):
#             c = random.random()
#             if (c <= r):
#                 for k in range(3):
#                     if (i[j+k] == 1.0) or (i[j+k] == 255):
#                         i[j+k] = 0
#                     else:
#                         i[j+k] = 255
#     return copy

#takes an image and a background color to overlay image upon. built these assuming an RGB image.
def preparerot(imge):
#     image = imge.copy()
    count = 0
    for i in range(imge.shape[0]): # for every pixel:
        for j in range(imge.shape[1]):
            if imge[i][j][0] < 127 and imge[i][j][1] < 127 and imge[i][j][2] < 127: #is [0, 0, 0]:
                #any value as long as it's converted later, and 0 < x < 3
#                 if (count % 40 == 0):
#                     print(imge[i][j])
#                     plt.figure()
#                     plt.imshow(imge)
                imge[i][j] = [10,10,10] #(0,0,0,0)#[10, 48 ,22] #[255, 192, 203]
                count += 1
                

    #print("preparerot: ", np.amax(imge))
#     print("preparerot")
#     plt.figure()
#     plt.imshow(imge)
    return imge

#takes an image and a background color to overlay image upon. built these assuming an RGB image.
# def preparerot(imge):
# #     image = imge.copy()
    
#     for i in range(imge.shape[0]): # for every pixel:
#         for j in range(imge.shape[1]):
#             if imge[i][j][0] != 255 and imge[i][j][1] != 255 and imge[i][j][2] != 255: #is [0, 0, 0]:
#                 #any value as long as it's converted later, and 0 < x < 3
#                 imge[i][j] = [10,10,10] #(0,0,0,0)#[10, 48 ,22] #[255, 192, 203]

#     #print("preparerot: ", np.amax(imge))
#     print("preparerot")
#     plt.figure()
#     plt.imshow(imge)
#     return imge



#need to do before applying noise
def rotateclean(imge, theta, color = None):
    if color == None:
        color = [255, 255, 255]
    
    image = imge.copy()
    #print("rotateclean: ", np.amax(image))
    image = preparerot(image)
    
    #1/17 dealing with blank output. temporary fix: rotate, compress, translate
    #print("rotate: ", np.amax(image))
    image = rotate(image, theta) * 255
    #print("rotate: ", np.amax(image))
    for i in range(image.shape[0]): # for every pixel:
        for j in range(image.shape[1]):
            if (image[i][j][0] != 10 and image[i][j][1] != 10 and image[i][j][2] != 10): #is [0, 0, 0]:
                image[i][j] = color
            else:
                image[i][j] = [0,0,0]
    
#     print("rotateclean")
#     plt.figure()
#     plt.imshow(image)
    return image

# def rotateclean(imge, theta, color = None):
#     if color == None:
#         color = [255, 255, 255]
    
#     image = imge.copy()
#     #print("rotateclean: ", np.amax(image))
#     image = preparerot(image)
    
#     #1/17 dealing with blank output. temporary fix: rotate, compress, translate
#     #print("rotate: ", np.amax(image))
#     image = rotate(image, theta) * 255
#     #print("rotate: ", np.amax(image))
#     for i in range(image.shape[0]): # for every pixel:
#         for j in range(image.shape[1]):
#             if (image[i][j][0] != 10 and image[i][j][1] != 10 and image[i][j][2] != 10): #is [0, 0, 0]:
#                 image[i][j] = color
#             else:
#                 image[i][j] = [0,0,0]
    
# #     print("rotateclean")
# #     plt.figure()
# #     plt.imshow(image)
#     return image


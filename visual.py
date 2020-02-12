"""
Top-Level Description
"""

#compress by a factor of x, any positive finite real number
def compressx(img, factor):
    sub1 = int((img.shape[0] - (img.shape[0] / factor)) / 2)
    sub2 = int((img.shape[1] - (img.shape[1] / factor)) / 2)
    
    im2 = imgwlarge.copy()
#    im2 = imgw.copy() #(use this line if input is 800x800)
    
    shrunk = resize(img.copy(), (int(img.shape[0] / factor), int(img.shape[1] / factor), int(img.shape[2]))) * 255
    
#     im2[100+sub1:100+(shrunk.shape[0]+sub1),200+sub2:200+(shrunk.shape[1]+sub2)] = shrunk
    im2[sub1:(shrunk.shape[0]+sub1),sub2:(shrunk.shape[1]+sub2)] = shrunk
    
    return im2
from PIL import Image
from numpy import asarray
# load the image
image = Image.open('new.png')
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
print(data)

[[[  7,  13,  75],
  [ 11, 12, 79],
  [ 20,  21,  86],
  [ 11,  18,  98],
  [ 11,  18,  98],
  [ 12,  19,  99]],

 [[  6,  10,  71],
  [  7,   7,  69],
  [ 15,  15,  77],
  [ 11,  18,  98],
  [238, 246, 207]],

 [[  0,   0,  28],
  [  0,   0,  27],
  [  2,   1,  32],
  [237, 245, 206],
  [242, 250, 211],
  [246, 254, 215]]]
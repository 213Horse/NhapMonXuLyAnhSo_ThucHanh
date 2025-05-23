import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

data = iio.imread("bird.png", as_gray=True)
plt.imshow(data, cmap='gray')
plt.title('Grayscale Image')
plt.show()





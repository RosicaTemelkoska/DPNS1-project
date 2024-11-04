import cv2
from skimage.metrics import structural_similarity as ssim

# Вчитај ја првата слика
image1 = cv2.imread('sliki/image1.jpeg', cv2.IMREAD_GRAYSCALE)
# Вчитај ја втората слика
image2 = cv2.imread('sliki/image2.jpeg', cv2.IMREAD_GRAYSCALE)

# Пресметај SSIM меѓу сликите
ssim_index = ssim(image1, image2)

print("SSIM индекс на сличност:", ssim_index)

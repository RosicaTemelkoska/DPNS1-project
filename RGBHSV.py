import cv2
import numpy as np

def show_image(image, window_name='Image'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def compare_images(image1, image2):
    # Convert images to HSV
    image1_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    image2_hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # Compute absolute difference in HSV
    diff_hsv = cv2.absdiff(image1_hsv, image2_hsv)
    diff_hsv = cv2.cvtColor(diff_hsv, cv2.COLOR_HSV2BGR)

    # Compute absolute difference in RGB
    diff_rgb = cv2.absdiff(image1, image2)

    # Display the difference images
    show_image(diff_hsv, 'Difference in HSV')
    show_image(diff_rgb, 'Difference in RGB')

if __name__ == "__main__":
    # Load images
    image1 = cv2.imread('sliki/image1.jpeg')
    image2 = cv2.imread('sliki/image2.jpeg')

    # Resize images to the same dimensions (optional)
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Compare images
    compare_images(image1, image2)

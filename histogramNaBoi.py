import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    image = cv2.imread(image_path)
    histogram = cv2.calcHist([image], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    return histogram

def plot_histogram(image_path, color):
    histogram = calculate_histogram(image_path)
    plt.plot(histogram.flatten(), color=color)

def print_histogram_difference(image1_path, image2_path):
    histogram1 = calculate_histogram(image1_path)
    histogram2 = calculate_histogram(image2_path)
    histogram_difference = np.abs(histogram1 - histogram2)
    print("Histogram Difference:")
    for i in range(256):
        for j in range(256):
            for k in range(256):
                if histogram_difference[i, j, k] != 0:
                    print(f"({i}, {j}, {k}): {histogram_difference[i, j, k]}")

# Патеки до сликите
image1_path = "sliki/image1.jpeg"
image2_path = "sliki/image2.jpeg"

# Прикажи ги хистограмите за секоја слика
plt.figure(figsize=(10, 5))
plot_histogram(image1_path, 'b')
plot_histogram(image2_path, 'r')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Color Histogram Comparison')
plt.legend(['Image 1', 'Image 2'])
plt.show()

# Испечати ја разликата помеѓу хистограмите
print_histogram_difference(image1_path, image2_path)

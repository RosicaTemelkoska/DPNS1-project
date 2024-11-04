import cv2
import numpy as np


def calculate_moments(image):
    # Convert image to grayscale manually
    gray = cv2.split(image)[0]  # Take only one channel (assuming it's grayscale)

    # Calculate moments
    moments = cv2.moments(gray)

    # Calculate centroid
    if moments["m00"] != 0:
        centroid_x = int(moments["m10"] / moments["m00"])
        centroid_y = int(moments["m01"] / moments["m00"])
    else:
        centroid_x, centroid_y = 0, 0

    # Calculate area
    area = moments["m00"]

    # Calculate orientation
    orientation = 0.5 * np.arctan2(2 * moments["mu11"], moments["mu20"] - moments["mu02"])

    return centroid_x, centroid_y, area, orientation


def draw_difference(image1, image2):
    # Calculate moments for both images
    centroid_x1, centroid_y1, area1, orientation1 = calculate_moments(image1)
    centroid_x2, centroid_y2, area2, orientation2 = calculate_moments(image2)

    # Display results
    print("Image 1:")
    print("Centroid (x, y):", centroid_x1, centroid_y1)
    print("Area:", area1)
    print("Orientation:", np.degrees(orientation1))
    print()
    print("Image 2:")
    print("Centroid (x, y):", centroid_x2, centroid_y2)
    print("Area:", area2)
    print("Orientation:", np.degrees(orientation2))
    print()
    print("Difference:")
    print("Centroid difference (x, y):", centroid_x1 - centroid_x2, centroid_y1 - centroid_y2)
    print("Area difference:", area1 - area2)
    print("Orientation difference:", np.degrees(orientation1) - np.degrees(orientation2))


if __name__ == "__main__":
    # Load images
    image1 = cv2.imread('sliki/image1.jpeg', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('sliki/image2.jpeg', cv2.IMREAD_GRAYSCALE)

    # Ensure images have the same dimensions
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Draw difference between moments
    draw_difference(image1, image2)

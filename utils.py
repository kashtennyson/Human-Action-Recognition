from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import hashlib

def get_unique_image_sizes(image_label_pairs):
    image_shapes = [Image.open(img_path).size for img_path, _ in image_label_pairs[:100]]
    unique_shapes = set(image_shapes)
    print("Unique image sizes:", unique_shapes)
    return unique_shapes

def plot_color_distribution(image_path):
    img = cv2.imread(image_path)
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
    plt.title("Color Distribution")
    plt.show()

def find_duplicates(image_label_pairs):
    hashes = {}
    for img_path, _ in image_label_pairs:
        img_hash = hash_image(img_path)
        if img_hash in hashes:
            print(f"Duplicate found: {img_path} and {hashes[img_hash]}")
        else:
            hashes[img_hash] = img_path

def hash_image(image_path):
    with open(image_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def check_corrupt_images(image_label_pairs):
    flag = 0
    for img_path, _ in image_label_pairs:
        try:
            img = Image.open(img_path)
            img.verify()  # Verify if it's a valid image
        except (IOError, SyntaxError):
            print(f"Corrupt image detected: {img_path}")
            flag = 1
    if flag == 0:
        print ("No corrupt image found in the dataset")
  

import cv2
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def get_pixel_coordinates(image_path, pixel_position):
    """
    Converts a pixel position within an image to its corresponding x and y coordinates.
    
    Args:
        image_path (str): Path to the image file.
        pixel_position (tuple): A tuple containing the pixel position (x, y).
    
    Returns:
        tuple: A tuple containing the x and y coordinates, the pixel value at that position, and the image.
    
    Raises:
        ValueError: If the image cannot be loaded or if the pixel position is out of bounds.
    """
    # Try loading the image with OpenCV first
    image = cv2.imread(image_path)
    
    if image is None:
        # If OpenCV fails, try using Pillow
        try:
            with Image.open(image_path) as img:
                image = np.array(img)
                if len(image.shape) == 2:  # Grayscale image
                    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
                elif image.shape[2] == 4:  # RGBA image
                    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
        except Exception as e:
            raise ValueError(f"Unable to load image: {e}")

    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Extract the x and y coordinates from the pixel position
    x, y = pixel_position
    
    # Handle negative indices
    x = width + x if x < 0 else x
    y = height + y if y < 0 else y

    if x >= width or y >= height or x < 0 or y < 0:
        raise ValueError("Pixel position out of bounds.")
    
    # Get the pixel value (for verification purposes)
    pixel_value = image[y, x].tolist()
    
    return x, y, pixel_value, image

def visualize_pixel(image, x, y):
    """
    Visualizes the specified pixel on the image with a red dot.
    
    Args:
        image (numpy.ndarray): The image array.
        x (int): The x-coordinate of the pixel.
        y (int): The y-coordinate of the pixel.
    """
    # Create a copy of the image to avoid modifying the original
    viz_image = image.copy()
    
    # Draw a red dot at the specified pixel location
    cv2.circle(viz_image, (x, y), 5, (0, 0, 255), -1)
    
    # Display the image
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(viz_image, cv2.COLOR_BGR2RGB))
    plt.title(f'Image with Pixel ({x}, {y}) Highlighted')
    plt.axis('off')
    plt.show()

def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: python pixel_to_coordinates.py <image_path> <x> <y> [--visualize]")
        return
    
    image_path = sys.argv[1]
    try:
        x = int(sys.argv[2])
        y = int(sys.argv[3])
    except ValueError:
        print("Error: x and y must be integers")
        return
    
    visualize = len(sys.argv) == 5 and sys.argv[4] == "--visualize"
    
    try:
        x, y, pixel_value, image = get_pixel_coordinates(image_path, (x, y))
        print(f"Pixel position: ({x}, {y})")
        print(f"X-coordinate: {x}")
        print(f"Y-coordinate: {y}")
        print(f"Pixel value (BGR): {pixel_value}")
        
        if visualize:
            visualize_pixel(image, x, y)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
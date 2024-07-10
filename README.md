
# Pixel to Coordinates Conversion Script

## Introduction
This Python script converts pixel locations within an image to their corresponding x and y coordinates. It demonstrates the ability to work with Python and solve a fundamental computer vision task, while also handling various image formats and edge cases. The script also includes a visualization feature to display the selected pixel on the image.

## Prerequisites
- Python 3.x
- OpenCV library
- Pillow library
- Matplotlib library (for visualization)

## Installation
To install the required libraries, you can use pip:

```bash
pip install opencv-python pillow matplotlib
```

## Running the Script
To run the script, use the following command in your terminal:

```bash
python pixel_to_coordinates.py <image_path> <x> <y> [--visualize]
```

Where:
- `<image_path>` is the path to your image file
- `<x>` is the x-coordinate of the pixel
- `<y>` is the y-coordinate of the pixel
- `--visualize` is an optional flag to display the image with the selected pixel highlighted

Examples:
```bash
python pixel_to_coordinates.py cat.jpg 100 50
python pixel_to_coordinates.py cat.jpg 100 50 --visualize
```

## Output
The script will display:
- The input pixel position
- The x-coordinate
- The y-coordinate
- The pixel value at the given position (in BGR format)

If the --visualize flag is used, it will also show the image with the selected pixel highlighted.

Example output:
```
Pixel position: (100, 50)
X-coordinate: 100
Y-coordinate: 50
Pixel value (BGR): [120, 140, 160]
```

## Features
- Supports various image formats (JPEG, PNG, BMP, etc.)
- Handles grayscale, RGB, and RGBA images
- Supports negative indexing for pixel coordinates
- Provides detailed error messages for better debugging
- Optional visualization of the selected pixel on the image

## Error Handling
The script includes error handling for various scenarios:
- Invalid image path or unsupported image format
- Out-of-bounds pixel coordinates
- Non-integer input for x and y coordinates

## Assumptions
- The script assumes that the user has the necessary permissions to read the image file.
- For color images, the pixel values are returned in BGR format (as used by OpenCV).
- The script expects integer values for x and y coordinates.

## Note
- Ensure you have the necessary permissions to read the image file and that the file path is correct.
- This script is designed for educational and demonstration purposes. For production use, additional error handling and optimizations may be necessary.

## How It Works
1. The script loads the image using OpenCV.
2. It checks if the provided coordinates are within the image boundaries.
3. If the coordinates are valid, it retrieves the pixel value at that location.
4. The script then returns and prints the x and y coordinates along with the pixel value.
5. If the --visualize flag is used, it displays the image with the selected pixel highlighted.

## Limitations
- The script does not handle image rotation or transformation.
- It does not provide image editing capabilities.

## Troubleshooting
If you encounter any issues:
- Ensure all prerequisites are correctly installed.
- Check that the image path is correct and the file exists.
- Verify that the provided coordinates are within the image dimensions.
- If visualization doesn't work, ensure matplotlib is correctly installed.

## Contributing
Feel free to fork this project and submit pull requests with any enhancements.


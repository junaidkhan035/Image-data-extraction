import cv2
import pytesseract
import re
import numpy as np
import matplotlib.pyplot as plt

# If Tesseract is not in your PATH, specify the executable path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed


# Function to preprocess the image
def preprocess_image(image):
    # Apply GaussianBlur to remove noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Show the preprocessed image
    plt.imshow(thresh, cmap='gray')
    plt.title('Preprocessed Image')
    plt.show()

    return thresh


# Extract text using pytesseract OCR
def extract_text(image):
    # Perform OCR on the image
    custom_config = r'--oem 3 --psm 6'  # Set OCR Engine Mode (OEM) and Page Segmentation Mode (PSM)
    text = pytesseract.image_to_string(image, config=custom_config)
    return text


# Function to categorize and extract information using regex
def extract_information(text):
    # Regex patterns
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'\b(?:\+?(\d{1,3})[-.\s]?|)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b')
    name_pattern = re.compile(r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b')  # Simplistic pattern for names
    address_pattern = re.compile(r'\d{1,5}\s\w+\s\w+')

    # Extract information
    email = email_pattern.findall(text)
    phone = phone_pattern.findall(text)
    name = name_pattern.findall(text)
    address = address_pattern.findall(text)

    return {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }


# Main function
def main(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    preprocessed_image = preprocess_image(image)
    text = extract_text(preprocessed_image)
    information = extract_information(text)

    print('Extracted Information:')
    for key, value in information.items():
        print(f'{key}: {value}')


# Example usage
main('imeagees.webp')

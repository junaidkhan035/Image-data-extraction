# Image-data-extraction
Step 1: Image Loading and Preprocessing
The first task of your code is to load an image and preprocess it to make it easier for the OCR (Optical Character Recognition) engine to extract text from it. This is crucial because images may contain noise, variations in lighting, or background elements that could hinder the text extraction process.

How it works:

The image is read in grayscale (black and white) using OpenCV. This simplifies the image by removing color information.
A Gaussian blur is applied to reduce noise. Gaussian blur smooths the image, which helps OCR focus on the main textual content.
Then, adaptive thresholding is applied. This converts the image into a binary form (black and white) where text is highlighted, and the background is mostly suppressed. Adaptive thresholding adjusts itself based on different regions of the image, which is useful when the lighting or background varies across the image.
Result: The output is a preprocessed image where the text is easier to recognize, and this image is displayed using a plot for verification.

Step 2: Extracting Text Using Tesseract OCR
After the image is preprocessed, it is passed to Tesseract OCR for text extraction. Tesseract is a powerful open-source OCR engine that converts images of text into machine-encoded text.

How it works:

Tesseract is configured with certain settings. The --oem 3 setting instructs it to use both the legacy OCR engine and the newer LSTM-based (neural network) engine to maximize accuracy.
The --psm 6 setting tells Tesseract to assume the image contains a single block of text, making it suitable for documents that have paragraphs or sentences in one continuous flow.
Result: The text that Tesseract extracts from the image is returned as a string, which can then be analyzed further.

Step 3: Categorizing and Extracting Information with Regex
Once the text is extracted, the code tries to identify specific types of information, such as email addresses, phone numbers, names, and addresses. It does this using regular expressions (regex), which are patterns designed to match certain kinds of text.

How it works:

Email Pattern: A regex is used to find email addresses by looking for text that follows the pattern of an email (e.g., something@domain.com).
Phone Number Pattern: The phone number regex is designed to match various formats of phone numbers, including international formats with or without country codes.
Name Pattern: A basic name pattern is used, which matches two capitalized words. While this is a simple approach, it works reasonably well for detecting first and last names, though it might not always be accurate.
Address Pattern: It uses a basic pattern that looks for a number followed by words, assuming this to be an address. This is a simple approach and may need adjustments for different formats of addresses.
Result:

The regex patterns search through the extracted text and pull out potential matches for emails, phone numbers, names, and addresses.
The extracted information is stored in a dictionary format with categories like "Name," "Phone," "Email," and "Address."

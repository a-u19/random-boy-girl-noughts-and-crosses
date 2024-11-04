import cv2
import pytesseract
from noughts_and_crosses import create_noughts_and_crosses_board, NoughtsAndCrossesDisplay
import tkinter as tk

# Set the path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image and perform OCR
def load_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError("The specified image file could not be found.")
    return image

# Enhanced preprocessing for OCR
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scale_percent = 200  # increase size by 200%
    width = int(gray.shape[1] * scale_percent / 100)
    height = int(gray.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(gray, dim, interpolation=cv2.INTER_CUBIC)
    _, thresh = cv2.threshold(resized, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

# Extract text using OCR
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Check for specific words in the extracted text
def check_for_words(text):
    if "girl" in text.lower():
        # print("The word 'girl' was found in the text.")
        create_noughts_and_crosses_board(winner="girl", file_path="noughts_and_crosses.png")
        return "girl"
    elif "boy" in text.lower():
        # print("The word 'boy' was found in the text.")
        create_noughts_and_crosses_board(winner="boy", file_path="noughts_and_crosses.png")
        return "boy"
    else:
        print("Neither 'boy' nor 'girl' was found in the text.")
        return None

# Main function
def main(file_path):
    try:
        # Load, preprocess, and perform OCR
        image = load_image(file_path)
        preprocessed_image = preprocess_image(image)
        text = extract_text(preprocessed_image)

        # Check for target words and display the Noughts and Crosses board if found
        winner = check_for_words(text)
        if winner:
            # Start the Tkinter display
            root = tk.Tk()
            app = NoughtsAndCrossesDisplay(root, "noughts_and_crosses.png")
            root.mainloop()
    except FileNotFoundError as e:
        print(e)

# Run the main function with the path to the image file
file_path = "boy_3.png"  # Replace with your image path
main(file_path)

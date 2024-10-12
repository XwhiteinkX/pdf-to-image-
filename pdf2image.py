import fitz  # PyMuPDF
import os

# Use absolute path
def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

# Specify the path of the PDF to be converted
directory = # Enter the path to the folder containing the PDF files here
files = get_all_files(directory)

for file in files:
    pdf_path = file

    # Define the path to save images (a folder named the same as the PDF file)
    save_path = os.path.join(os.path.dirname(pdf_path), os.path.splitext(os.path.basename(pdf_path))[0])

    # Create the save path if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Open PDF file
    doc = fitz.open(pdf_path)

    # Iterate through each page of the PDF
    for page_number in range(len(doc)):
        # Get the page object
        page = doc.load_page(page_number)

        # Convert the PDF page to an image (pix object)
        pix = page.get_pixmap(dpi=300)  # Set DPI to 300

        # Define the save path and file name for the image
        image_path = os.path.join(save_path, f'page_{page_number + 1}.png')

        # Save image
        pix.save(image_path)

    # Close the document object
    doc.close()

print("PDF conversion completed.")

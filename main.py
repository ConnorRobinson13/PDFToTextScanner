import os
import glob
import PyPDF2

# Set the directory containing the PDF files
pdf_dir = "input"

# Check if the directory exists
if not os.path.exists(pdf_dir):
    raise ValueError("The specified directory does not exist")

# Initialize an empty list to store the text from the PDF files
pdf_text = []

# Use glob to get a list of all PDF files in the directory
pdf_files = glob.glob(pdf_dir + "/*.pdf")

# Check if there are any PDF files in the directory
if not pdf_files:
    raise ValueError("No PDF files found in the specified directory")

# Iterate through each PDF file
for file in pdf_files:
    # Open the PDF file in read-only mode
    with open(file, 'rb') as pdf:
        # Create a PDF object
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        # Iterate through each page of the PDF
        for page in range(pdf_reader.getNumPages()):
            # Get the text from the current page
            page_text = pdf_reader.getPage(page).extractText()
            # Add the text to the list
            pdf_text.append(page_text)

# Join the text from all the PDFs into a single string
all_text = '\n'.join(pdf_text)

# Set the output file path
output_file = "output/output.txt"

# Create the output directory if it does not already exist
if not os.path.exists("output"):
    os.makedirs("output")

# Write the text to a file
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(all_text)

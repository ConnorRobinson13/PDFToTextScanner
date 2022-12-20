import tkinter as tk
from tkinter import filedialog

import PyPDF2


def select_files():
    # Open a file selection dialog
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    # Get a list of the selected file paths
    file_paths = list(files)
    # Check if any files were selected
    if not file_paths:
        return
    # Initialize an empty list to store the text from the PDF files
    pdf_text = []
    # Iterate through each PDF file
    for file in file_paths:
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
    # Open a save file dialog
    output_file = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")], defaultextension=".txt")
    # Check if the user cancelled the save dialog
    if not output_file:
        return
    # Write the text to the selected file
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(all_text)


# Create the GUI
root = tk.Tk()
root.title("PDF Converter")

# Create a label to explain how to use the program
instructions = tk.Label(root,
                        text="To use this program, click the 'Select PDF files' button and select the PDF files you "
                             "want to convert. Then choose a location to save the output file.")
instructions.pack()

# Create a button to select the files
select_button = tk.Button(root, text="Select PDF files", command=select_files)
select_button.pack()

# Run the GUI
root.mainloop()

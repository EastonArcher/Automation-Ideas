import PyPDF2
import sys
import os

# Initialize a PdfFileMerger object from PyPDF2 library
merger = PyPDF2.PdfFileMerger()

# Iterate through all files in the current directory
for file in os.listdir(os.curdir):
    # Checking if the file ends with ".pdf"
    if file.endswith(".pdf"):
        # If the file is a PDF, append it to the merger object
        merger.append(file)
    merger.write("Combined.pdf")

import os
from PyPDF2 import PdfFileReader, PdfFileMerger

current_directory = os.getcwd()
all_files = list()

# Add in main text file.
pdf_files = [file for file in os.listdir(current_directory) if file.endswith('.pdf')]

# Merge the files
merger = PdfFileMerger()
for file in pdf_files:
    merger.append(PdfFileReader(file), 'rb')

merger.write('merged_pdf.pdf')

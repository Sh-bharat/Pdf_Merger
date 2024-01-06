from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    merger = PdfMerger()
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    merger.write(output_path)
    merger.close()

def get_user_input():
    pdf1_path = input("Enter the path of the first PDF file: ")
    pdf2_path = input("Enter the path of the second PDF file: ")
    output_path = input("Enter the name for the output merged PDF file: ")

    return pdf1_path, pdf2_path, output_path

if __name__ == "__main__":
    pdf1, pdf2, output = get_user_input()

    if not (os.path.exists(pdf1) and os.path.exists(pdf2)):
        print("One or both input files do not exist.")
    else:
        merge_pdfs(pdf1, pdf2, output)


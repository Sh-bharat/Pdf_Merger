---

## PDF Merger in Python

### Overview
This Python script facilitates merging two PDF files into a single document using the PyPDF2 library. It prompts the user to input the paths for both PDFs to be merged and designates a name for the output merged PDF file.

### Requirements
- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

### Usage
1. **Run the Script:**
   - Execute the `mergepdf.py` file.
  
2. **Input Paths:**
   - Enter the paths for the two PDF files when prompted.
  
3. **Specify Output Name:**
   - Provide a name for the merged PDF file.

### Code Structure
```python
# mergepdf.py
from PyPDF2 import PdfMerger
import os

# Function to merge PDFs
def merge_pdfs(pdf1_path, pdf2_path, output_path):
    merger = PdfMerger()
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    merger.write(output_path)
    merger.close()

# Function to get user input
def get_user_input():
    pdf1_path = input("Enter the path of the first PDF file: ")
    pdf2_path = input("Enter the path of the second PDF file: ")
    output_path = input("Enter the name for the output merged PDF file: ")

    return pdf1_path, pdf2_path, output_path

# Main function
if __name__ == "__main__":
    pdf1, pdf2, output = get_user_input()

    if not (os.path.exists(pdf1) and os.path.exists(pdf2)):
        print("One or both input files do not exist.")
    else:
        merge_pdfs(pdf1, pdf2, output)
```

### Notes
- Ensure both input PDF files exist at the provided paths.
- The merged PDF file will be created with the specified output name.


--- 

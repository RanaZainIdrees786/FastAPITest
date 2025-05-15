import pandas as pd
import fitz  # PyMuPDF


def read_excel_data(file_path ):
    df = pd.read_excel(file_path)
    df_string = df.to_string()
    return df_string
0
def read_pdf_data(file_path):
    # Open the PDF
    doc = fitz.open(file_path)
    # Join text from all pages into a single string
    pdf_text = "\n".join([page.get_text() for page in doc])
    # Optional: close the document
    doc.close()
    # Now pdf_text contains the full PDF text as a string
    return pdf_text


if __name__ == "__main__":
    # print(read_excel_data('data/Courses.xlsx'))
    pdf_path = "data/Arfa Karim Technology Incubator.pdf"  # Replace with your actual file path
    print(read_pdf_data(pdf_path))


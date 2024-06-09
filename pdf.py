from PyPDF2 import PdfReader, PdfWriter


# create a python method to select a subset of the pdf pages and save it under a new name
def select_pdf_pages(pdf_path, start_page, end_page, new_pdf_path):
    pdf = PdfReader(pdf_path)
    writer = PdfWriter()
    for i in range(start_page, end_page):
        writer.add_page(pdf.pages[i])
    with open(new_pdf_path, 'wb') as f:
        writer.write(f)


if __name__ == '__main__':
    input_pdf = "/Users/janbanot/downloads/Updated.pdf"
    output_pdf = "/Users/janbanot/downloads/JanBanot_CV.pdf"
    select_pdf_pages(input_pdf, 0, 1, output_pdf)

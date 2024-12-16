import PyPDF2
import argparse
import os


def interleave_pdfs(odd_pdf_path, even_pdf_path, output_pdf_path):
    # Open the input PDF files
    with open(odd_pdf_path, 'rb') as odd_file, open(even_pdf_path, 'rb') as even_file:
        odd_reader = PyPDF2.PdfReader(odd_file)
        even_reader = PyPDF2.PdfReader(even_file)

        # Create a PdfWriter object to write the merged content
        pdf_writer = PyPDF2.PdfWriter()

        # Get the total number of pages in each PDF
        odd_pages = len(odd_reader.pages)
        even_pages = len(even_reader.pages)

        # Interleave pages: odd pages first, then even pages in reverse order
        for i in range(odd_pages):
            # Add the odd page
            pdf_writer.add_page(odd_reader.pages[i])

            # Add the corresponding even page (in reverse order)
            if i < even_pages:
                pdf_writer.add_page(even_reader.pages[even_pages - 1 - i])

        # Write the output to the new PDF
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
odd_pdf = 'odd_pages.pdf'  # PDF with odd pages
even_pdf = 'even_pages.pdf'  # PDF with even pages in reverse order
output_pdf = 'merged_output.pdf'  # Output PDF

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--document-name", type=str, help="Supply the document name, without _even.pdf or _odd.pdf")
parser.add_argument("-o", "--output-file", type=str, help="Supply the output document name. Defaults to <document_name>_all.pdf")
args = parser.parse_args()

if args.output_file is None:
    args.output_file = f"{args.document_name}_all.pdf"

document_name = os.path.expanduser(args.document_name)

interleave_pdfs(f"{document_name}_odd.pdf", f"{document_name}_even.pdf", args.output_file)

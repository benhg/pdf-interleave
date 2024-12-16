# PDF Interleave

Imagine this scenario. You have gone to scan some documents that are double sided. But your scanner cannot handle double-sided. The document has too many pages to scan individually in a flatbed scanner, flipping each time.

A strike of brilliance hits your mind. You will place your document in face-up, scan all the odd pages, then flip the stack over and put it back in, scanning the even pages.

However, this leaves you with two documents:

1. The odd pages in increasing order (1,3,5,7,etc)
2. The even pages in decreasing order (100,98,96,etc)

This project solves just that situation.

# Usage

1. Name your two documents the same thing, but differing by _even and _odd
2. Run the tool `pdf_interleave.py -d <document_name>`. Don't put _even or _odd, or .pdf in the document name.
3. The output will go to `<document_name>_all.pdf`
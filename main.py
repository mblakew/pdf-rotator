import PyPDF2

file_path = input("Enter pdf to rotate...\n")

file_in = open(file_path, "rb")

reader = PyPDF2.PdfFileReader(file_in)
writer = PyPDF2.PdfFileWriter()

for page_index in range(reader.numPages):
    page = reader.getPage(page_index)
    page.rotateClockwise(90)
    writer.addPage(page)

file_out = open("result.pdf", 'wb')
writer.write(file_out)
file_in.close()
file_out.close()



# pdf_in = open(file_in, "rb")
# pdf_reader = PyPDF2.PdfFileReader(pdf_in)
# pdf_writer = PyPDF2.PdfFileWriter()

# for pagenum in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(pagenum)
    
#     page.rotateClockwise(90)
#     pdf_writer.addPage(page)

# pdf_out = open('rotated.pdf', 'wb')
# pdf_writer.write(pdf_out)
# pdf_out.close()
# pdf_in.close()
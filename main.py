import PyPDF2

file_path = input("Enter pdf to rotate...\n")

file = open(file_path, "rb")

reader = PyPDF2.PdfFileReader(file)
writer = PyPDF2.PdfFileWriter()

for page_index in range(reader.numPages):
    page = reader.getPage(page_index)
    page.rotateClockwise(90)
    writer.addPage(page)


file_out = open("rotated.pdf", "wb")

writer.write(file_out)
file.close()
file_out.close()
### UNDER DEVELOPMENT ###
import PyPDF2


# create a filename
filename = input("enter the .pdf filename: ")
if filename == "":
    filename = "ADM0722JUL22_test.pdf"
else:
    filename = filename
# print(filename)

# read the pdf file
with open(filename,'rb') as fhandle:

    # create a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(fhandle)

    # print num pages
    num_pages = pdfReader.numPages
    # print(f'Pages in the pdf file: {num_pages}.\n')

    # get a page
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

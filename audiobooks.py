import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
bookName = input("Enter name of the PDF: ")
book = open(bookName, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
totalPages = pdfReader.numPages
print("Total pages in the PDF = {}".format(totalPages))
pageNumber = int(input("Which page do you want me to start reading from? "))
for num in range (pageNumber -1, totalPages, 1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
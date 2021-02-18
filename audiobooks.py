import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
bookName = input("Enter name of the PDF: ")
book = open(bookName, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pageNumber = input("Enter the page number you want to me read: ")
page = pdfReader.getPage(pageNumber - 1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
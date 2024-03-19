from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime
import os

# from DocxTemplate import doxcTemplate


class converWordToPdf:

    def __init__(self, FileNameDoc, FileNamePDF):
        self._fileNameDoc = FileNameDoc
        self._fileNamePDF = FileNamePDF
    

    def CreatePdfFile(self):

        if(os.path.isfile(self._fileNamePDF)):
             os.remove(self._fileNamePDF)
            
        print("Create the PDF File")
        convert(self._fileNameDoc, self._fileNamePDF)
        print("Finished creating the PDF file")


    def RemoveDocxFile(self):
        print("Remove " + self._fileNameDoc)
        os.remove(self._fileNameDoc)
        print("Done removing " + self._fileNameDoc)



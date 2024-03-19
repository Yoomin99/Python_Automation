from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime
import os
from UserInterface import userInput


class doxcTemplate:
    def __init__(self , fileNameOfTemplate , FileNameDoc):
        self._fileNameOfTemplate = fileNameOfTemplate
        self._fileNameDoc = FileNameDoc
        self._docxTemplate = DocxTemplate(self._fileNameOfTemplate)
    
    def createUpdatedWordFile(self, updatedInput : userInput):
        context = {
            'today_date' : updatedInput.today_date,
            'company_name' : updatedInput.company_name,
            'position_name' : updatedInput.position_name
        }
        
        self._docxTemplate.render(context)
        #it will create the new file with updated inputs
        self._docxTemplate.save(self._fileNameDoc)
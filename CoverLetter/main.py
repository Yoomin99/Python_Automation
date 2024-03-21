import sys

from DocxTemplate import doxcTemplate
from UserInterface import userInput
from ConvertFromWordToPDF import converWordToPdf

language = ["skip" , "CSharp" , "Javascript" , "C" , "Golang"]

def main() -> int:
   
    
    user = userInput()
    user.getUserInput()
    fileNameOfTemplate = "Template/CoverLetter_template" + "_" + language[user.lang] + ".docx"
    
    fileNameDoc = "CoverLetter_" + user.company_name + ".docx"
    fileNamePDF = "CoverLetter/CoverLetter_" + user.company_name + ".pdf"


    doc = doxcTemplate(fileNameOfTemplate ,fileNameDoc )
    doc.createUpdatedWordFile(user)

    convert = converWordToPdf(fileNameDoc , fileNamePDF)
    convert.CreatePdfFile()
     
    convert.RemoveDocxFile()

    return 0



if __name__ == '__main__':
    sys.exit(main()) 


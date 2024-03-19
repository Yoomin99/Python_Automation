from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime
import os

class userInput:
    def __init__(self):
        self.company_name = ""
        self.position_name = ""
        self.today_date = ""

    
    def getUserInput(self):
        self.company_name = input("Enter name of the company: ")
        self.position_name = input("Enter name of the position: ")
        self.today_date = datetime.datetime.today().strftime('%B %d, %Y')
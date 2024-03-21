from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime
import os

class userInput:
    def __init__(self):
        self.company_name = ""
        self.position_name = ""
        self.today_date = ""
        self.lang = ""

    
    def getUserInput(self):
        self.company_name = input("Enter name of the company: ")
        self.position_name = input("Enter name of the position: ")
        
        print("Select the language:  ")
        print("1: C#")
        print("2: Javascript")
        print("3: C/C++")
        print("4: Golang")
        self.lang = int(input("Enter the programming language: "))

        if(self.lang < 1 or self.lang > 4):
            print("Invalid boundary")
            exit
        



        self.today_date = datetime.datetime.today().strftime('%B %d, %Y')
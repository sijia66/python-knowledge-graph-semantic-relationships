import wikipedia
import os


class TextExtractor:

    def __init__(self, pageTitle, pageId):
        self.__pageTitle = pageTitle
        self.__pageId = pageId
    
    def extract(self):
        page = wikipedia.page(title=self.__pageTitle, pageid=self.__pageId)

        if not os.path.isdir('text'):
            os.mkdir('text')
            print(f'created text folder in {os.getcwd()}')
        
        with open("./text/" + self.__pageTitle + ".txt", "w", encoding='utf-8') as f:
            f.write(page.content)

    def getText(self):
        flnm = "./text/" + self.__pageTitle + ".txt"
        try:
            f = open(flnm , "r")
            f_ctent = f.read()
            return f_ctent
        except:
            print('cannot open the file:')
            print(flnm)

 
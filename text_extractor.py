import wikipedia


class TextExtractor:

    __pageTitle: str
    __pageId: str

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
        f = open("./text/" + self.__pageTitle + ".txt", "r")
        return f.read()

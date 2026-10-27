class Document:
    def __init__(self, content):
        self.content = content


class Printer:
    def print_document(self, document):
        print(document.content)


document = Document("Hello, Python!")
printer = Printer()

printer.print_document(document)
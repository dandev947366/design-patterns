'''
https://en.wikipedia.org/wiki/Interface_segregation_principle
'''


class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError
        
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass
        
class OldFashionedPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan')
        
        
        
        
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass
        
class MyPrinter(Printer):
    def printer(self, document):
        print(document)
        
class Photocopier(Printer, Scanner):
    def print(self, document):
        pass
    def scan(self, document):
        pass
    
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
        
    @abstractmethod
    def scan(self, document):
        pass
        
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer
    def print(self, document):
        self.printer.print(document)
    def scan(self, document):
        self.scanner.scan(document)
'''
SRP SOC
The single-responsibility principle (SRP) is a computer programming principle that states that "A module should be responsible to one, and only one, actor."[1] The term actor refers to a group (consisting of one or more stakeholders or users) that requires a change in the module.

Source: https://en.wikipedia.org/wiki/Single-responsibility_principle
'''

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
        
    def remove_entry(self, pos):
        del self.entries[pos]
        
    def __str__(self):
        return '\n'.join(self.entries)
        
   
    #NOTE - against single responsibility design principle
    # secondary responsibility
    '''
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    def load(self, filename):
        pass
    def load_from_web(self, uri):
        pass
    '''
    
    
    #NOTE - Solution : not overload object with too many responsibilities
class PersistenceManager():
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
    
    
j = Journal()
j.add_entry('I play tennis today')
j.add_entry('I go go shopping in the evening')
print(f'Journal entries: \n{j}')

file = r'../../test.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
class Note():
    #Class variable
    __next_id = 1

    def __init__(self,tag,memo):
        self.__tag = tag
        self.__memo = memo
        #self.__create_date = date.today()
        self.__id = Note.__next_id
        Note.__next_id +=1

    def get_tag(self):
        return self.__tag

    def get_memo(self):
        return self.__memo

    def __str__(self):
        return f'{self.__id} {self.__tag} {self.__memo}'
    def __eq__(self,other):
        if other is None:
            return False
        if isinstance(other, Note) == False:
            return False
        return (self.__tag ==  other.__tag and self.__memo == other.__memo)

class Notebook():
    def __init__(self):
        self.__notes = []

    def new_note(self,tag=None, memo=None, note_obj=None):
        if note_obj is not None:
            new_note = note_obj
        else:
            new_note = Note(tag,memo)
            if new_note in self.__notes:
                return False
            else:
                self.__notes.append(new_note)
                return True

    def __str__(self):
        output = ''
        for n in self.__notes:
            output += str(n) + '\n'
        return output
    def search(self,keyword):
        search_result = []
        for n in self.__notes:
            if keyword in n.get_tag() or keyword in n.get_memo():
                search_result.append(n)
        return search_result
    def load(self):
        data = [['Work', 'Team meeting on Friday'],
                ['Work', 'Assignment due soon'],
                ['Friend', 'Ball game this week'],
                ['Friend', 'Movie'],
                ['Home', 'Visit relatives']]
        for value in data:
            self.__notes.append(Note(value[0],value[1]))

def test_search():
    nb = Notebook()
    nb.load()
    print(nb)
    print("Search for Work")
    result = nb.search("Work")
    for n in result:
        print(n)

    result = nb.search('Assignment')
    print("Search for Assignment")
    for n in result:
        print(n)
def test_NoteBook():
    nb = Notebook()
    #Add Note Object to the Notebook object
    nb.add_note("Work","Friday 10am meeting")

    n1 = Note("School work", "Start working on assignment")
    nb.add_note(note_obj=n1)
    nb.add_note(note_obj=n1)
    print(nb)
    nb.load()
    print(nb)

def test_note():
    n1 = Note("School work", "Start working on assignment 1")
    n2 = Note("School work", "Prepare for test")
    n3 = Note("School work", "Prepare for test")

    print(n1)
    print(n2)
    print(n3)
    #Comparing objects
    print(n1==n2)
    print(n2==n3)
    print(n2==None)
    print(n2== "Hello python")

def main():
    #test_note()
    #test_NoteBook()
    test_search()
    print('End')

if __name__ =="__main__":
    main()
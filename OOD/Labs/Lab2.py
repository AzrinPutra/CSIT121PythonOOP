#driver or client class - "View"
#Non Object-Oriented - try to turn this into "Object-Oriented"
#NoteBook_App class

from NoteBook import Note,Notebook

def menuOption():
    print("Notebook Menu\n")
    print("1. Show all notes")
    print("2. Search Notes")
    print("3. Add Notes")
    print("4. Modify Notes")
    print("5. Quit")
    choice = int(input("Enter an option:" ))
    return choice

def search_notes(notebook):
    filter = input("Enter filter:")
    notes = notebook.search(filter)

    print("Search Results: ")
    print_notes(notes)

def print_notes(notes):
    print("#"*20)
    for note in notes:
        print(note)
    print("#"*20)

def add_notes(notebook):
    memo = input("Enter memo: ")
    tags = input("Enter tags: ")
    notebook.new_note(memo,tags)
    print("New note added")

def modify_note(notebook):
    id = int(input("Enter note id:"))
    note = notebook.find_note(id)
    if note:
        memo = input("Enter new memo: ")
        tags = input("Enter new tags: ")
        if memo:
            notebook.modify_memo(id,memo)
        if tags:
            notebook.modify_tags(id,tags)
    else:
        print("Invalid note id")

def show_all_notes(notebook):
    print(notebook)

def main():
    notebook = Notebook()
    notebook.new_note("test1","tagA")
    notebook.new_note("test2","tagB")
    notebook.new_note("test3","tagC")
    carryon = True
    while carryon:
        choice = menuOption()
        if choice==1:
            show_all_notes(notebook)
        elif choice==2:
            search_notes(notebook)
        elif choice==3:
            add_notes(notebook)
        elif choice==4:
            modify_note(notebook)
        elif choice==5:
            carryon=False
        else:
            print("Invalid choice")
    print("End of notebook")

main()
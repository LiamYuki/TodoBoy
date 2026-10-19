from todo import Todo
from datetime import date

def test_todo():
    entry = Todo('Test')
    assert(entry.message == 'Test')
    assert(entry.finished == False)
    assert(entry.date == date.today())

    entry.edit('New message')
    assert(entry.message == 'New message')
    assert(entry.date == date.today())

    entry.complete()
    assert(entry.finished == True)

    print(entry.content())
    print('Todo tests passed')

if __name__ == '__main__':
    test_todo()
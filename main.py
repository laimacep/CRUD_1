
from demo_data import *
from list_CRUD import *
id_counter = 3

while True:
    view_options()
    option = input()
    match option:
        case '1':
            print('You chose to see all authors')
            view_authors(authors)
        case '2':
            id_counter = add_author(id_counter, authors)
        case '3':
            edit_author(authors)
        case '4':
            delete_author(authors)
        case '5':
            print('You chose to exit the page')
            break
        case _:
            print('You chose an invalid option')
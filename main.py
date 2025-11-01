from list_CRUD import *
id_counter = 3
book_id_counter = 6

while True:
    view_options()
    option = input()
    match option:
        case '1':
            choice = selection()
            if choice == 'authors':
                view_authors(authors)
            elif choice == 'books':
                view_books(books)
            elif choice == 'all':
                view_all(authors, books)
        case '2':
            choice = selection()
            if choice == 'authors':
                id_counter = add_author(id_counter, authors)
            elif choice == 'books':
                book_id_counter = add_book(book_id_counter, books)
        case '3':
            choice = selection()
            if choice == 'authors':
                edit_author(authors)
            elif choice == 'books':
                edit_book(books)
        case '4':
            choice = selection()
            if choice == 'authors':
                delete_author(authors)
            elif choice == 'books':
                delete_book(books)
        case '5':
            print('You chose to exit the page')
            break
        case _:
            print('You chose an invalid option')
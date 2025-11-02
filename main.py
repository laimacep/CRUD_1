from list_CRUD import *
import operator
id_counter = 3
book_id_counter = 6

while True:
    view_options()
    option = input()
    match option:
        case '1':
            option = (input(f'Select what you want to view: \n 1. Authors    2. Books    3. All\n').lower().strip(' .'))
            if option in ('1', '1.authors', 'authors'):
                view_authors(authors)
            elif option in ('2', '2.books', 'books'):
                view_books(books)
            elif option in ('3', '3.all', 'all'):
                view_all(authors, books)
            else:
                print('Ooops, a typo. Try again!')
        case '2':
            choice = selection()
            if choice == 'authors':
                id_counter = add_author(id_counter, authors)
            elif choice == 'books':
                book_id_counter, id_counter = add_book(book_id_counter,id_counter, authors, books)
        case '3':
            choice = selection()
            if choice == 'authors':
                edit_author(authors)
            elif choice == 'books':
                edit_book(books)
        case '4':
            choice = selection()
            if choice == 'authors':
                delete_author(authors,books)
            elif choice == 'books':
                delete_book(books)
        case '5':
            choice = selection()
            if choice == 'authors':
                sorted_authors = sorted(authors, key=operator.itemgetter('name'))
                for i in sorted_authors:
                    print(f' {i['author_id']}. {i['name']} {i['surname']}')
            elif choice == 'books':
                sorted_books = sorted(books, key=operator.itemgetter('title'))
                for i in sorted_books:
                    print(f' {i['book_id']}. {i['title']}')
        case '6':
            print('Nothing to do, huh? Buh-bye then!')
            break
        case _:
            print('Ooops, a typo. Try again!')


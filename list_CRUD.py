import re

from demo_data import *

def view_options():
    print(f'Choose what you want to do:\n 1. View...\n 2. Add... \n 3. Edit... \n 4. Delete... \n 5. Exit page')

def selection():
    option = (input(f'Select what you want to view: \n 1. Authors    2. Books    3. All\n').lower().strip(' .'))
    if option in ('1', '1.authors', 'authors'):
        return 'authors'
    if option in ('2', '2.books', 'books'):
        return 'books'
    if option in ('3', '3.all', 'all'):
        return 'all'
    else:
        print('You chose an incorrect value')
        return None

def view_authors(authors):
    for author in authors:
        print(f'{author['author_id']}. {author['name']} {author['surname']}')

def view_books(books):
    for book in books:
        print(f'{book['book_id']}. {book['title']} {book['genre']}')

def view_all(authors, books):
    for author in authors:
        print(f'{author["name"]} {author["surname"]}')
        author_books = [book for book in books if book['author_id'] == author["author_id"]]
        if author_books:
            for book in author_books:
                print(f' - {book["title"]} {book["genre"]}')
        else:
            print(f'No books found for {author["name"]}')

def add_author(id_counter,authors):
    print('You chose to add a new author')
    print('Write the name of the new author')
    name = input()
    print('Write the surname of the new author')
    surname = input()
    id_counter += 1
    new_author = {'author_id': id_counter, 'name': name, 'surname': surname}
    authors.append(new_author)
    return id_counter

def add_book(book_id_counter,books):
    print('You chose to add a new book')
    print('Write the tile of the new book')
    title = input()
    print('Write the genre of the new book')
    genre = input()
    book_id_counter += 1
    new_book = {'book_id': book_id_counter, 'title': title, 'genre': genre}
    books.append(new_book)
    return book_id_counter

def edit_author(authors):
    print('You chose to edit an author')
    print('Select which author you want to edit')
    view_authors(authors)
    edit_author_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, edit_author_id):
        for i, author in enumerate(authors):
            if str(author['author_id']) == edit_author_id:
                print('Write new author name')
                authors[i]['name'] = input()
                print('Write new author surname')
                authors[i]['surname'] = input()
        else:
            print('You chose and invalid id')
    else:
        print('You chose and invalid id')

def edit_book(books):
    print('You chose to edit a book')
    print('Select which book you want to edit')
    view_books(books)
    edit_book_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, edit_book_id):
        for i, book in enumerate(books):
            if str(book['book_id']) == edit_book_id:
                print('Write new book title')
                books[i]['title'] = input()
                print('Write new book genre')
                books[i]['genre'] = input()
        else:
            print('You chose and invalid id')
    else:
        print('You chose and invalid id')

def delete_author(authors):
    print('You chose to delete an author')
    print('Select which author id you want to delete')
    view_authors(authors)
    del_author_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, del_author_id):
        for i, author in enumerate(authors):
            if str(author['author_id']) == del_author_id:
                print(f'Are you sure you want to delete this author?')
                print('Type 0 to confirm delete and 1 to exit')
                confirmation = input()
                if confirmation == '0':
                    for author in authors:
                        if str(author['author_id']) == del_author_id:
                            authors.remove(author)
                            break
                if confirmation == '1':
                    pass
        else:
            print('You chose and invalid id')
    else:
        print('You chose and invalid id')

def delete_book(books):
    print('You chose to delete a book')
    print('Select which book you want to delete')
    view_books(books)
    del_book_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, del_book_id):
        for i, book in enumerate(books):
            if str(book['book_id']) == del_book_id:
                print(f'Are you sure you want to delete this book?')
                print('Type 0 to confirm delete and 1 to exit')
                confirmation = input()
                if confirmation == '0':
                    for book in books:
                        if str(book['book_id']) == del_book_id:
                            books.remove(book)
                            break
                if confirmation == '1':
                    pass
        else:
            print('You chose and invalid id')
    else:
        print('You chose and invalid id')
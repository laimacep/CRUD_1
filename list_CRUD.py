import re
from demo_data import load_authors
from demo_data import load_books

def get_a_id(authors=None):
    if authors is None:
        authors = []
    max_id = 0
    for a in authors:
        if int(a['author_id']) > max_id:
            max_id = int(a['author_id'])
    return max_id

def get_b_id(books=None):
    if books is None:
        books = []
    max_id = 0
    for b in books:
        if int(b['book_id']) > max_id:
            max_id = int(b['book_id'])
    return max_id

def view_options():
    print(f'Choose what you want to do:\n 1. View...\n 2. Add... \n 3. Edit... \n 4. Delete...\n 5. Sort...\n 6. Exit page')

def selection():
    option = (input(f'Select which data you want to work with: \n 1. Authors    2. Books\n').lower().strip(' .'))
    if option in ('1', '1.authors', 'authors'):
        return 'authors'
    if option in ('2', '2.books', 'books'):
        return 'books'
    else:
        print('Ooops, a typo. Try again!')
        return None

def view_authors(authors):
    for author in authors:
        print(f'{author['author_id']}. {author['name']} {author['surname']}')

def view_books(books):
    for book in books:
        print(f'{book['book_id']}. {book['title']} / {book['genre']}')

def view_all(authors, books):
    for author in authors:
        print(f'{author['name']} {author['surname']}')
        author_books = [book for book in books if book['author_id'] == author['author_id']]
        if author_books:
            for book in author_books:
                print(f' - {book['title']} / {book['genre']}')
        else:
            print(f'No books found for {author['name']}')

def add_author(id_counter,authors):
    print('You chose to add a new author')
    print('Write the name of the new author')
    name = input().title()
    print('Write the surname of the new author')
    surname = input().title()
    existing_a = None
    for author in authors:
        if author['name'].lower() == name.lower() and author['surname'].lower() == surname.lower():
            existing_a = author
            print('Seriously?! The author is already in the list...')
    if not existing_a:
        id_counter += 1
        new_author = {'author_id': id_counter, 'name': name, 'surname': surname}
        authors.append(new_author)
        print(f'New author {new_author['name']} {new_author['surname']} added')
    return id_counter

def add_book(book_id_counter,id_counter, authors, books):
    print('You chose to add a new book')
    print('Please enter the author of the new book')
    name = input(f'Enter the name of the author: ').title()
    surname = input('Enter the surname of the author: ').title()
    existing_author = None
    for author in authors:
        if author['name'].lower() == name.lower() and author['surname'].lower() == surname.lower():
            existing_author = author
            break
    if not existing_author:
        id_counter += 1
        new_author = {'author_id': id_counter, 'name': name, 'surname': surname}
        authors.append(new_author)
        existing_author = new_author
    print('Write the tile of the new book')
    title = input().strip().title()
    print('Write the genre of the new book')
    genre = input().strip().title()
    book_id_counter += 1
    new_book = {'book_id': book_id_counter,'author_id':existing_author['author_id'], 'title': title, 'genre': genre}
    books.append(new_book)
    return book_id_counter, id_counter

def edit_author(authors):
    print('You chose to edit an author')
    print('Select which author you want to edit')
    view_authors(authors)
    edit_author_id = input()
    allowed = r'^[\d]+$'
    if re.match(allowed, edit_author_id):
        for i, author in enumerate(authors):
            if str(author['author_id']) == edit_author_id:
                print('Write new author name')
                authors[i]['name'] = input()
                print('Write new author surname')
                authors[i]['surname'] = input()
    else:
        print('Hmmm.. Type the ID of the author!')

def edit_book(books):
    print('You chose to edit a book')
    print('Select which book you want to edit')
    view_books(books)
    edit_book_id = input()
    allowed = r'^[\d]+$'
    if re.match(allowed, edit_book_id):
        for i, book in enumerate(books):
            if str(book['book_id']) == edit_book_id:
                print('Write new book title')
                books[i]['title'] = input()
                print('Write new book genre')
                books[i]['genre'] = input()
    else:
        print('Hmmm.. Type the ID of the book!')

def delete_author(authors,books):
    print('You chose to delete an author')
    print('Select which author id you want to delete')
    view_authors(authors)
    del_author_id = input()
    allowed = r'^[\d]+$'
    if re.match(allowed, del_author_id):
        del_author = next((author for author in authors if author['author_id'] == del_author_id),None)
        if del_author is None:
            print('You chose and invalid id')
        print(f'Are you sure you want to delete author {del_author['name']} {del_author['surname']}?')
        print('Type YES to confirm delete and NO to cancel. REALLY THINK ABOUT IT!')
        confirmation = input().lower()
        if confirmation == 'yes':
            authors[:] = [a for a in authors if a['author_id'] != del_author_id]
            books[:] = [b for b in books if b['author_id'] != del_author_id]
            print(f'Congrats, you deleted {del_author['name']} {del_author['surname']}. AND ALL HIS BOOKS! You dummy!')
        elif confirmation == 'no':
            print('Good. You made the right decision. Less work later on...')
    else:
        print('Hmmm.. Type the ID of the author!')

def delete_book(books):
    print('You chose to delete a book')
    print('Select which book you want to delete')
    view_books(books)
    del_book_id = input()
    allowed = r'^[\d]+$'
    if re.match(allowed, del_book_id):
        for book in books:
            if book['book_id'] == del_book_id:
                print(f'Are you sure you want to delete {book['title']}?')
                print('Type YES to confirm delete and NO to cancel. REALLY THINK ABOUT IT!')
                confirmation = input().lower()
                if confirmation == 'yes':
                    books[:] = [b for b in books if b['book_id'] != del_book_id]
                    print(f'Congrats, you deleted {book['title']}. Now what?')
                if confirmation == 'no':
                    print('Good. You made the right decision. Less work later on...')
    else:
        print('Hmmm.. Type the ID of the book!')
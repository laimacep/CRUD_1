import re
import mysql
import mysql.connector

from secret import DB_CONFIG

headers_authors = ['author_id', 'name', 'surname']
headers_books = ['book_id','author_id', 'title', 'genre']

def get_a_id(authors=[]):
    return 0

def get_b_id(books=[]):
    return 0

def view_options():
    print(f'Choose what you want to do:\n 1. View...\n 2. Add... \n 3. Edit... \n 4. Delete...\n 5. Sort...\n 6. Exit page')

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_authors():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from authors')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    authors = []
    for row in rows:
        item = {}
        for i in range(len(headers_authors)):
            item[headers_authors[i]] = row[i]
        authors.append(item)
    return authors

def load_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from books')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    books = []
    for row in rows:
        item = {}
        for i in range(len(headers_books)):
            item[headers_books[i]] = row[i]
        books.append(item)
    return books

def view_authors(authors):
    authors = load_authors()
    for author in authors:
        print(f'{author['author_id']}. {author['name']} {author['surname']}')

def view_books(books):
    books = load_books()
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

def selection():
    option = (input(f'Select which data you want to work with: \n 1. Authors    2. Books\n').lower().strip(' .'))
    if option in ('1', '1.authors', 'authors'):
        return 'authors'
    if option in ('2', '2.books', 'books'):
        return 'books'
    else:
        print('Ooops, a typo. Try again!')
        return None

def add_author(a='',authors=[]):
    print('You chose to add a new author')
    print('Write the name of the new author')
    name = input().title()
    print('Write the surname of the new author')
    surname = input().title()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute('insert into authors (name, surname) values (%s, %s)',(name, surname))
    conn.commit()
    # new_author = {'author_id': cur.lastrowid, 'name': name, 'surname': surname}
    # authors.append(new_author)
    cur.close()
    conn.close()

def delete_author(authors,books):
    print('You chose to delete an author')
    print('Select which author id you want to delete')
    view_authors(authors)
    del_author_id = input()

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('select name, surname from authors where author_id = %s',(del_author_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    print(f'Are you sure you want to delete author {result}?')
    print('Type YES to confirm delete and NO to cancel. REALLY THINK ABOUT IT!')
    confirmation = input().lower()
    if confirmation == 'yes':

        conn = get_conn()
        cur = conn.cursor()
        cur.execute('delete from authors where author_id = %s',(del_author_id,))
        conn.commit()
        cur.close()
        conn.close()

    elif confirmation == 'no':
        print('Good. You made the right decision. Less work later on...')

def delete_book(books):
    print('You chose to delete a book')
    print('Select which book you want to delete')
    view_books(books)
    del_book_id = input()

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('delete from books where book_id = %s', (del_book_id,))
    conn.commit()
    cursor.close()
    conn.close()

    # allowed = r'^[\d]+$'
    # if re.match(allowed, del_book_id):
    #     for book in books:
    #         if book['book_id'] == del_book_id:
    #             print(f'Are you sure you want to delete {book['title']}?')
    #             print('Type YES to confirm delete and NO to cancel. REALLY THINK ABOUT IT!')
    #             confirmation = input().lower()
    #             if confirmation == 'yes':
    #                 books[:] = [b for b in books if b['book_id'] != del_book_id]
    #                 print(f'Congrats, you deleted {book['title']}. Now what?')
    #             if confirmation == 'no':
    #                 print('Good. You made the right decision. Less work later on...')
    # else:
    #     print('Hmmm.. Type the ID of the book!')
import csv

from demo_data import load_authors
from demo_data import load_books

headers_authors = ['author_id', 'name', 'surname']
headers_books = ['book_id', 'author_id', 'title', 'genre']

def get_a_id(authors=[]):
    f = open('files/author_id.txt')
    return int(f.read())
def save_a_id(id):
    with open('files/author_id.txt', 'w') as f:
        f.write(id)

def load_authors():
    with open('authors.csv', mode ='r', encoding ='utf-8') as file:
        return list(csv.DictReader(file))

def save_authors(authors):
    with open('authors.csv', mode ='w',newline='', encoding ='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers_authors)
        writer.writeheader()
        writer.writerows(authors)

def view_authors(authors):
    for author in authors:
        print(f'{author['author_id']} {author['name']} {author['surname']}')

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
        save_authors(authors)
        print(f'New author {new_author['name']} {new_author['surname']} added')
    return id_counter
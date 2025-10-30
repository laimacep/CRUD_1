import re
def view_options():
    print('Choose what you want to do:')
    print('1. View all authors')
    print('2. Add a new author')
    print('3. Edit an author')
    print('4. Delete an author')
    print('5. Exit page')

def view_authors(authors):
    for author in authors:
        print(f'{author['id']}. {author["name"]} {author["surname"]}')

def add_author(id_counter,authors):
    print('You chose to add a new author')
    print('Write the name of the new author')
    name = input()
    print('Write the surname of the new author')
    surname = input()
    id_counter += 1
    new_author = {'id': id_counter, 'name': name, 'surname': surname}
    authors.append(new_author)
    return id_counter

def edit_author(authors):
    print('You chose to edit an author')
    print('Select which author id you want to edit')
    view_authors(authors)
    edit_author_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, edit_author_id):
        for i, author in enumerate(authors):
            if str(author['id']) == edit_author_id:
                print('Write new author name')
                authors[i]['name'] = input()
                print('Write new author surname')
                authors[i]['surname'] = input()
    else:
        print('You chose and invalid id')

def delete_author(authors):
    print('You chose to delete an author')
    print('Select which author id you want to delete')
    view_authors(authors)
    del_author_id = input()
    allowed = r"^[\d]+$"
    if re.match(allowed, del_author_id):
        for author in authors:
            print(f'Are you sure you want to delete this author?')
            print('Type 0 to confirm delete and 1 to exit')
            confirmation = input()
            if confirmation == '0':
                authors.remove(author)
                break
            if confirmation == '1':
                break
    else:
        print('You chose and invalid id')


# Užduotis Biblioteka. Sukurti tokį pat veikiantį CRUDą su autoriais.
import re

authors = [{
    'id' : '1',
    'name' : 'Jane',
    'surname' : 'Austen'
},
    {
        'id' : '2',
        'name' : 'George',
        'surname' : 'Orwell'
},
    {
        'id' : '3',
        'name' : 'Toni',
        'surname' : 'Morrison'
    }
]

id_counter = 3

while True:
    print('Choose what you want to do:')
    print('1. View all authors')
    print('2. Add a new author')
    print('3. Edit an author')
    print('4. Delete an author')
    print('5. Exit page')

    option = input()
    match option:
        case '1':
            print('You chose to see all authors')
            for object in authors:
                print(*[str(k) + ':' + ' ' + str(v) for k, v in object.items()])
        case '2':
            print('You chose to add a new author')
            print('Write the name of the new author')
            name = input()
            print('Write the surname of the new author')
            surname = input()
            id_counter += 1
            new_author = {'id' : id_counter, 'name' : name, 'surname' : surname }
            authors.append(new_author)
        case '3':
            print('You chose to edit an author')
            print('Select which author id you want to edit')
            edit_author_id = input()
            allowed = r"^[0-9]+$"
            if re.match(allowed, edit_author_id):
                for i,author in enumerate(authors):
                    if str(author['id'])==edit_author_id:
                        print(*[str(k) + ':' + ' ' + str(v) for k, v in author.items()])
                        print('Write new author name')
                        authors[i]['name'] = input()
                        print('Write new author surname')
                        authors[i]['surname'] = input()
            else:
                print('You chose and invalid id')
        case '4':
            print('You chose to delete an author')
            print('Select which author id you want to delete')
            del_author_id = input()
            allowed = r"^[0-9]+$"
            if re.match(allowed, del_author_id):
                for object in authors:
                    print(f'Are you sure you want to delete author {object['id']}: {object['name']} {object['surname']}?')
                    print('Yes or No')
                    confirmation = input()
                if confirmation == del_author_id:
                    authors.remove(object)  #still in progress about the confirmation
            else:
                print('You chose and invalid id')
        case '5':
            print('You chose to exit the page')
            break
        case _:
            print('You chose an invalid option')
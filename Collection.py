import json
from collections import defaultdict

data_file = 'data.json'

data = defaultdict(list)

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file)

def load_data():
    try:
        with open(data_file, 'r') as file:
            json.load(file)

    except FileNotFoundError:
        return defaultdict(list)

def create_item(category, title, author, genre):
    item = {'Title': title, 'Author': author, 'Genre': genre}
    data[category].append(item)
    save_data()
    print(f'{category} has been added!')


def list_item(category):
    items = data[category]
    if not items: 
        print(f'{category} was not found in the list.')
    else: 
        for i, item in enumerate(items, start = 1):
            print(f'{category} #{i}: {item}')

    

def delete_item():
    pass

def update_item():
    pass
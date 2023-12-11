import Collection

def main():
    data = Collection.load_data()

    while True:
        
        print('1. Create Item \n2. List Item(s) \n3. Update Item \n4.Delete Item \n5. Exit App')
        choice = input('What would you like to do (1-4): ')


        if choice == 1:
            category = input('Enter category: ')
            title = input('Enter title: ')
            author = input('Enter author: ')
            genre = input('Enter genre: ')
            Collection.create_item(category, title, author, genre)

        if choice == 2:
            category = input('Enter category (books, cards, or cds): ').lower
            Collection.read_items(category)

        if choice == 3:
            category = input("Enter category (books, cards, cds): ").lower()
            index = int(input(f'Enter what you {category} you would like to update')) - 1
            title = input(f'Enter new {category} title')
            author = input(f'Enter new {category} author: ')
            genre = input(f'Enter new {category} genre: ')
            Collection.update_item(category, index, title, author, genre)

        if choice == 4:
            category = input('Enter category (books, cards, cds): ').lower()
            index = int(input(f'Enter {category} to delete: ')) - 1
            Collection.delete_item(category, index)


        if choice == 5:
            print('Thank you for using my app!')
            break

        else:
            print('Invalid selection.')

main()
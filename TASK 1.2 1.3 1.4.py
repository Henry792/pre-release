import pickle
class BookData:
    def __init__(self, unique_code, title, main_author, year_of_publication):
        self.unique_code = unique_code
        self.title = title
        self.main_author = main_author
        self.year_of_publication = year_of_publication


book_list = []
for i in range(10):
    unique_code = int(input('please input the unique code'))
    title = input('please input the title of the book')
    main_author = input('please input the main author')
    year_of_publication = input('please input the year of publication')
    book_list.append(BookData(unique_code, title, main_author, year_of_publication))

for i in range(10):
    print('information for book number', i, end=' ')
    print('unique code is', book_list[i].unique_code, end=' ')
    print('title is', book_list[i].title, end=' ')
    print('main author is', book_list[i].main_author, end=' ')
    print('year of publication is', book_list[i].year_of_publication)


def storing_records():
    book_file = open('book file.bin', 'wb')
    for i in range(10):
        pickle.dump(book_list[i], book_file)
    book_file.close()


def getting_name():
    for i in range(10):
        book_file = open('book file.bin', 'rb')
        book_record = pickle.load(book_file)
        print('information for book number', i, end=' ')
        print('unique code is', book_record.unique_code, end=' ')
        print('title is', book_record.title, end=' ')
        print('main author is', book_record.main_author, end=' ')
        print('year of publication is', book_record.year_of_publication)

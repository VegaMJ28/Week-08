import pickle

class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def add_book(self):
        self.book_id = int(input("Enter book id: "))
        self.book_title = input("Enter book title: ")
        self.author_id = int(input("Enter author id: "))
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = int(input("Enter year of publication: "))

    def display_book(self):
        print("BOOK INFO")
        print("Book id: ", self.book_id)
        print("Book title: ", self.book_title)
        print("Author id: ", self.author_id)
        print("Publisher: ", self.publisher)
        print("Year of publication: ", self.year_of_publication)

#main
bk1 = Book()
bk1.add_book()
bk1.display_book()

file1 = open("myBooks.dat","wb")
pickle.dump(bk1,file1)
file1.close()

file2 = open("myBooks.dat","rb")
#for line in file2:
    #print(line)


while 1:
    try:
        data = pickle.load(file2)
        print(data.book_id)
        print(data.book_title)
        print(data.author_id)
    except EOFError:
        break
file2.close()


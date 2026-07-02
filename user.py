class User:
    def __init__(self,user_id,name,password):
        self.user_id = user_id
        self.name=name
        self.password = password
        self.borrowed_books = []
    def login(self,password):
        if self.password == password:
            print('login successful')
            return True
        else:
            print('invalid password')
            return False
    def borrow_book(self,book):
        if book.is_available():
            self.borrowed_books.append(book.book_id)
            book.set_quantity(book.get_quantity()-1)
            print(f'{book.title} borrowed successfully')
        else:
            print('book is not available')

    def return_book(self,book):
        if book.book_id in self.borrowed_books:
            self.borrowed_books.remove(book.book_id)
            book.set_quantity(book.get_quantity() +1)
            print(f'{book.title} returned successfully')
        else:
            print('this book is not borrowed')
    def view_borrowed_book(self):
        if len(self.borrowed_books) ==0:
            print('no books borrowed')
        else:
            for i in self.borrowed_books:
                print(i)
    def display_user(self):
        print("User ID :", self.user_id)
        print("Name :", self.name)
        print("Borrowed Books :", self.borrowed_books)
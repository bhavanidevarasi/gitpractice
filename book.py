class Book:
    def __init__(self, book_id, title, author,category,price,quantity):
        self.book_id=book_id
        self.title = title
        self.author = author
        self.category = category
        self.__price = price
        self.__quantity = quantity
    def display_book(self):
        print('book id :',self.book_id)
        print('title :',self.title)
        print('author :',self.author)
        print('category :',self.category)
        print('price :',self.__price)
        print('quantity :',self.__quantity)

    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_price(self,price):
        if price > 0:
            self.__price = price
        else:
            print('invalid price')

    def set_quantity(self,quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print('invalid price')

    def is_available(self):
        if self.__quantity > 0:
            return 'Available'
    
    def update_book(self , title=None, author=None, category=None, price=None, quantity=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if category is not None:
            self.category = category
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
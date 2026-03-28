# class First():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def add(self):
#         return self.x + self.y
        
    
#     def subtract(self):
#         return self.x - self.y
    
#     def divide(self):
#         if self.y == 0:
#             return "Cannot divide by zero"
#         return self.x / self.y
    
#     def __str__(self):
#         return f" x = {self.x}, y={self.y}"
    

# calc = First(0,10)
# calc2 = First(20,30)

# print(calc.add())
# print(calc.divide())
# print(calc)
# print(calc2)



class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, title, author):
        book = {"title" : title, "author" : author, "available" : True}
        self.books.append(book)
        print(f"{title} by {author} has been added")
        
    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if book['available']:
                    book['available'] = False
                    print(f"{book['title']} has been borrowed.")
                else:
                    print(f"{book['title']} not available")
                return
        print(f"Book not Found")
        
    def return_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if not book['available']:
                    book['available'] = True
                    print(f"{book['title']} has been returned.")
                else:
                    print(f"{book['title']} available")
                return
        print(f"Book not Found")
        
    def available_books(self):
        for book in self.books:
            if book['available']:
                print(f"{book['title']}")
                
    def __str__(self):
        available = len([ book for book in self.books if book['available']])
        return f"{self.name} | {len(self.books)} | {available}"
            
        

lib = Library("City Library")
lib.add_book("Python Crash Course", "Eric Matthes")
lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
lib.add_book("1984", "Goerge Orwell")
lib.borrow_book("1984")
lib.borrow_book("The Great Gatsby")
lib.return_book("1984")
lib.available_books()
print(lib)

        
        
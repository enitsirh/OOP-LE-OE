class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Your Name", "Makoto Shinkai")
print(f"Book Title: {book.title}\nAuthor: {book.author}\n")


book2 = Book("Painter of the Night", "Byeonduck")
print(f"Book Title: {book2.title}\nAuthor: {book2.author}\n")

del book.author


book2 = Book("Painter of the Night", "Byeonduck")
print(f"Book Title: {book2.title}\nAuthor: {book2.author}\n")

print(f"Book Title: {book.title}\nAuthor: {book.author if hasattr(book, 'author') else 'Author not available'}\n")
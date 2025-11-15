# Aggregation = Represents a relationship where one object (the whole)
#               contains references to one or more INDEPENDENT objects (the parts)

from library import Library, Book

library = Library("New Yorl Public Library")

book1 = Book("Harry Potter....", "J.K Rowling")

book2 = Book("The Hobbit", "J.R.R. Tolkein")

book3 = Book("The colour of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(book)
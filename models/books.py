from models.book import *

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book2 = Book("Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction")
book3 = Book("Alice's Adventures in Wonderland", "Lewis Carroll", "Fiction")

list_of_books = [book1, book2, book3]

def add_new_book_to_list(book):
    list_of_books.append(book)

def remove_book_from_list(book_title):
    book_to_remove = None
    for book in list_of_books:
        if book.title == book_title:
            book_to_remove = book
            break
    list_of_books.remove(book_to_remove)

# def delete_event(event_name):
#     event_to_delete = None
#     for event in events:
#         if event.name == event_name:
#             event_to_delete = event
#             break

#     events.remove(event_to_delete)

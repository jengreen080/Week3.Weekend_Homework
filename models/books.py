from models.book import *

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "'Shoot all the Bluejays you want, if you can hit 'em, but remember it's a sin to kill a Mockingbird.' Atticus Finch gives this advice to his children as he defends the real mockingbird of this classic novel - a black man charged with attacking a white girl. Through the eyes of Scout and Jem Finch, Lee explores the issues of race and class in the Deep South of the 1930s with compassion and humour. She also creates one of the great heroes of literature in their father, whose lone struggle for justice pricks the conscience of a town steeped in prejudice and hypocrisy.", "5 stars")
book2 = Book("Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction","It's an ordinary Thursday lunchtime for Arthur Dent until his house gets demolished. The Earth follows shortly afterwards to make way for a new hyperspace express route, and his best friend has just announced that he's an alien. At this moment, they're hurtling through space with nothing but their towels and an innocuous-looking book inscribed, in large friendly letters, with the words: DON'T PANIC.","5 stars")
book3 = Book("Alice's Adventures in Wonderland", "Lewis Carroll", "Fiction", "Alice’s collected adventures in the blazingly surreal Wonderland constitute nothing less than the beginning of modern fiction for children. Populated by a cast of unforgettable characters from the White Rabbit to the Queen of Hearts, as well as an addictive internal logic all their own, Carroll’s remarkable works fizz with imagination and invention.", "5 stars")

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

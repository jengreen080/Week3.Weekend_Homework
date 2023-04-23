from app import app
from flask import render_template, request, redirect
from models.books import *

@app.route('/books/')
def index():
    return render_template('index.html', title = 'Home', books = list_of_books)

@app.route('/books/', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    description = request.form['description']
    rating = request.form['rating']
    #   recurring = True if 'recurring' in request.form else False
    new_book = Book(title, author, genre, description, rating)
    add_new_book_to_list(new_book)
    return redirect('/books/')

@app.route('/books/delete/<title>', methods=['POST'])
def delete_book(title):
    remove_book_from_list(title)
    return redirect('/books/')

@app.route('/books/<index>')
def selected_book(index):
    selected_book = list_of_books[int(index)]
    return render_template('book.html', book = selected_book)

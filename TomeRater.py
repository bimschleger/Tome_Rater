class User(object):
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.eamil = address
        print(f'The email address for {self.name} has been updated')

    def __repr__(self):
        return 'User: {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        i = 0
        ratings_sum = 0

        for rating in self.books.values():  # self.books has key/value pairs for book/rating
            ratings_sum += rating
            i += 1

        average_rating = ratings_sum / i
        return average_rating

# Create the book Class

class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn_new):
        self.isbn = isbn_new
        print('Updated ISBN for {}. New ISBN is: {}'.format(self.title, self.isbn))

    # Adds the book rating to the overall Book object.

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid rating.')

    # Checks to see if one book is the same as the other.

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        i = 0
        ratings_sum = 0

        for rating in self.ratings:
            ratings_sum += rating
            i += 1

        average_rating = ratings_sum / i
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


class Nonfiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '{}, a {} manual on {}'.format(self.title, self.level, self.subject)

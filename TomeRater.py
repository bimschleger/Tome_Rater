class User(object):
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}                 # Key: Book object, Value: Rating

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(f'The email address for {self.name} has been updated')

    def __repr__(self):
        return 'User: {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        if rating != None:
             self.books[book] = rating

    def get_average_rating(self):
        i = 0
        ratings_sum = 0

        for rating in self.books.values():  # self.books has key/value pairs for book/rating
            try:
                ratings_sum += rating
                i += 1
            except TypeError:
                continue

        average_rating = ratings_sum / i
        return average_rating


# Create the book Class

class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []


    # Returns the Title of the Book

    def get_title(self):
        return self.title


    # Returns the ISBN of the Book

    def get_isbn(self):
        return self.isbn


    # Overwrite the existing ISBN with a new ISBN

    def set_isbn(self, isbn_new):
        self.isbn = isbn_new
        print('Updated ISBN for {}. New ISBN is: {}'.format(self.title, self.isbn))


    # Adds the book rating to the overall Book object.

    def add_rating(self, rating = None):
        try:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
        except TypeError:
            print('Invalid rating.')


    # Checks to see if one book is the same as the other.

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False


    # Return the average rating for a Book

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


# Sets up the Fiction subclass of Book

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


# Sets up the Nonfiction subclass of Book

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


# Creates the overall TomeRater class object

class TomeRater(object):
    def __init__(self):
        self.users = {}     # Key = User email. Value = User object.
        self.books = {}     # Key: Book object. Value: num times read by Users.


    # Creates a new Book class

    def create_book(self, title, isbn):
        book1 = Book(title, isbn)
        return book1


    # Creates a new Fiction class

    def create_novel(self, title, author, isbn):
        book1 = Fiction(title, author, isbn)
        return book1


    # Creates a new Nonfiction class

    def create_non_fiction(self, title, subject, level, isbn):
        book1 = Nonfiction(title, subject, level, isbn)
        return book1


    # Adds a Book to a User

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users.keys():
            print('No user with the email {}!'.format(email))
        else:
            user = self.users[email]
            user.read_book(book, rating)
            if isinstance(rating, int):
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1


    # Creates a new User and adds some books to them

    def add_user(self, name, email, user_books = None):
        user_new = User(name, email)
        self.users[user_new.email] = user_new

        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, user_new.email)


    # Prints the books in the Applicaiton

    def print_catalog(self):
        for i in self.books.keys():
            print(i.title)


    # Prints the list of Users in the applications

    def print_users(self):
        for i in self.users.values():
            print(i)


    # Print out the Book that has been read the most times

    def most_read_book(self):
        most_read_number = 0

        for book, number in self.books.items():
            if number > most_read_number:
                most_read_book = book
                most_read_number = number

        return most_read_book


    # Returns the highest rated book1

    def highest_rated_book(self):
        i = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if i == 0:
                highest_rating = rating
                highest_rating_book = book
            if rating > highest_rating:
                highest_rating = rating
                highest_rating_book = book
            i += 1

        return highest_rating_book


    # Returns the User with the highest average ratingself.

    def most_positive_user(self):
        i = 0
        for user in self.users.values():
            rating = user.get_average_rating()
            if i == 0:
                highest_rating = rating
                highest_rating_user = user
            if rating > highest_rating:
                highest_rating = rating
                highest_rating_user = user
            i += 1

        return highest_rating_user

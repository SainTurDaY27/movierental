# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from datetime import datetime


def make_movies():
    movies = [
        Movie("The Irishman", "2017", ["Children"]),
        Movie("CitizenFour", str(datetime.now().year), ["Horror"]),
        Movie("Frozen", "2002", ["Documentary"]),
        Movie("El Camino", str(datetime.now().year), ["Children"]),
        Movie("Particle Fever", "2016", ["Sci-Fi"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())

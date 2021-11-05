import csv
from enum import Enum
from datetime import datetime


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2.0 + 1.5 * (days - 2),
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + 1.5 * (days - 3),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent_renter_point(self, days):
        """Return the rental point for a given number of days"""
        frp = self.value["frp"]
        return frp(days)

    @classmethod
    def for_movie(cls, movie):
        """Method that identify the type of movie depending on its price code."""
        price_code = cls.normal
        if movie.get_year() == str(datetime.now().year):
            price_code = cls.new_release
        elif "Children" in movie.get_genre():
            price_code = cls.childrens
        return price_code


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def is_genre(self, genre):
        for i in self.__genre:
            if i == genre:
                return True

    def __str__(self):
        return self.__title


class MovieCatalog:
    """
    Method that manage data in movies.csv.
    """
    def __init__(self):
        self.data = []

    def read_data(self):
        """Method that will open & read each row of data in movies.csv"""
        with open("movies.csv", "r") as raw_data:
            rows = list(csv.reader(raw_data))
            for i in range(len(rows)):
                self.data.append(Movie(rows[i][1], rows[i][2], rows[i][3].split(sep='|')))

    def get_movie(self, title):
        """Method that will return a movie that have same title of input movie."""
        for i in self.data:
            if i == title:
                return self.data[i]
            else:
                self.read_data()

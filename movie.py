import csv


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
        """Method that will return true if genre match one of the movie's genre."""
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

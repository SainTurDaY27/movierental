import unittest
from rental import Rental
from movie import *
from datetime import datetime


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("El Camino", str(datetime.now().year), ["Children"])
        self.regular_movie = Movie("Frozen", "2002", ["Documentary"])
        self.childrens_movie = Movie("The Irishman", "2017", ["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("My movie", "2002", ["Drama"])
        self.assertEqual("My movie", m.get_title())

    def test_rental_price(self):
        """Tests for method get_price() for returning rental price"""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 7)
        self.assertEqual(rental.get_price(), 9.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3)

    def test_rental_points(self):
        """Tests for method get_renter_point() for returning rental point"""
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_renter_point(), 5.0)
        rental = Rental(self.new_movie, 7)
        self.assertEqual(rental.get_renter_point(), 7.0)
        rental = Rental(self.regular_movie, 6)
        self.assertEqual(rental.get_renter_point(), 1.0)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_renter_point(), 1.0)


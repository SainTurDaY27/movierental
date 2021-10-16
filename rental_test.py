import unittest
from customer import Customer
from rental import Rental
from movie import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", PriceCode.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", PriceCode.REGULAR)
        self.childrens_movie = Movie("Frozen", PriceCode.CHILDRENS)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", PriceCode.REGULAR)
        self.assertEqual("CitizenFour", m.get_title())
        self.assertEqual(PriceCode.REGULAR, m.get_price_code())

    def test_rental_price(self):
        """Tests for method get_price() for returning rental price"""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 7)
        self.assertEqual(rental.get_price(), 9.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)

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


import unittest
from datetime import datetime
from movie.movie import MovieNight


class TestMovieNight(unittest.TestCase):
    def setUp(self):
        self.movie = MovieNight("Baby Sky")

    def test_that_user_can_add_movie_to_the_movie_cart(self):
        self.movie.add_movie("The baby lion")
        self.movie.add_movie("Walking Dead")
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 2)
        self.movie.add_movie("Baby Lion")
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 3)

    def test_that_user_cannot_add_movie_twice_in_the_same_movie_cart(self):
        self.movie.add_movie("The baby lion")
        self.movie.add_movie("Walking Dead")
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 2)
        self.movie.add_movie("The baby lion")

    def test_that_user_can_rate_movie_in_the_movie_cart(self):
        self.movie.add_movie("The baby lion")
        self.movie.add_movie("Walking Dead")
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 2)
        self.movie.rate_movie("The baby lion",7.8)

    def test_that_user_can_remove_movie_from_the_movie_cart(self):
        self.movie.add_movie("Future Tells")
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 1)
        remove = self.movie.remove_movie("Future Tells")
        self.assertEqual(remove, True)
        number = self.movie.get_number_of_movies()
        self.assertEqual(number, 0)


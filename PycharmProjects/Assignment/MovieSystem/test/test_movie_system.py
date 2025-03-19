import unittest

from movie.movie_system import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("Bby Sky", "mountain")

    def test_initial_state_of_the_app_is_off(self):
        self.assertTrue(self.user.get_status, False)

    def test_that_movie_app_is_un_locked(self):
        self.user.unlock()
        self.assertTrue(self.user.get_status, True)

    def test_that_movie_app_is_locked(self):
        self.user.is_lock()
        self.assertTrue(self.user.get_status, False)

    def test_that_movie_app_cannot_be_accessed_without_credentials(self):
        self.user.unlock()
        self.assertEqual(self.user.get_username(), "Bby Sky")
        self.assertEqual(self.user.get_password(), "mountain")


if __name__ == '__main__':
    unittest.main()

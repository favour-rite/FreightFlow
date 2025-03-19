from datetime import datetime


class MovieNight:
    def __init__(self,title):
        self.title = title
        self.date_added = datetime.datetime.now()
        self.rating = 0
        self.number = 0
        self.movie_cart = []


    def add_movie(self, movie_name: str):
        if movie_name in self.movie_cart:
            self.movie_cart.append(movie_name)
            print(f"Movie {movie_name} is already in {self.movie_cart}.")
        else:
            print(f"Movie {movie_name} not available.")


    def get_number_of_movies(self):
        pass

    def remove_movie(self, movie_name: str):
        for movie_name in self.movie_cart:
            if movie_name in self.movie_cart:
                self.movie_cart.remove(movie_name)
                print(f"Movie {movie_name} has been removed from {self.movie_cart}.")
            else:
                print(f"Movie {movie_name} is not in {self.movie_cart}.")

    def rate_movie(self, movie_name: str, rate: float):
        for movie_name in self.movie_cart:
            if movie_name == movie_name:
                if 1 <= rate <= 5:
                    self.rating += rate
                else:
                    return ValueError('rating must be between 1 and 5')
            else:
                return ValueError('Movie name does not exist')
        return f'Movie {movie_name} has been rated to {self.rating}.'

    def get_average_rating(self):
        if not self.rating:
            return 0
        else:
            return sum(self.rating) / len(self.rating)

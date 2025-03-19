from datetime import datetime
from movie.movie_system import User
from movie.movie import Movie
class Main:

    @classmethod
    def main_menu(cls):
        print("""
                    Welcome to Skye Movie System!......
            *** Customer Satisfaction, Our Priority ***
            1. -> Add Movie.
            2. -> Rate Movie.
            3. -> Get Average Rating Movie.
            4. -> Get Average Ratings For All Movie .
            5. -> Remove Movie.
            6. -> Exit.
            """)
        Main.users_choice()

    @classmethod
    def users_choice(cls):
        choice = int(input("Input Your Choice: "))
        if choice == 1:
            Main.add_movie()
        elif choice == 2:
            Main.rate_movie()
        elif choice == 3:
            Main.average_rating_movie()
        elif choice == 4:
            Main.average_rating_for_all_movie()
        elif choice == 5:
            Main.remove_movie()
        elif choice == 6:
            Main.exit()
        else:
            print("Invalid Option. Try again......")
            Main.main_menu()

    @classmethod
    def add_movie(cls):
        try:
            title = input("Input title: ").strip().lower()
            Main.movie.add_movie(title)
        except ValueError as e:
            print("Invalid title. Try again......")

        print("Movie has been created")
        Main.main_menu()

    @classmethod
    def rate_movie(cls):
        try:
            title = input("Input title of movie to rate: ").split().lower
            if not title:
                raise ValueError("Invalid Movie Title")

            Main.movie.rate_movie(title)
        except ValueError:
            print("Invalid title. Try again......")
        Main.main_menu()

    @classmethod
    def average_rating_movie(cls):
        title = input("Input title to view: ")
        Main.movie.rate_movie(title)
        Main.main_menu()


    @classmethod
    def remove_movie(cls):
        title = input("Input title of movie to delete: ")
        Main.movie.remove_movie(title)
        Main.main_menu()

    @classmethod
    def average_rating_for_all_movie(cls):
        pass

    @classmethod
    def exit(cls):
        print("Exiting the application... Thanks For Using Skye Movie System")
        exit()




if __name__ == "__main__":
    Main.main_menu()
